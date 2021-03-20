from actions.models import Action
from actions.utils import create_action
from common.decorators import ajax_required
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.utils.http import urlsafe_base64_decode
from django.views.decorators.http import require_POST
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from account.models import Contact

from .models import Profile
from .serializers import UserSerializer
from .tasks import activation_email, add


@api_view(["POST"])
def activate(request):
    try:
        email = urlsafe_base64_decode(request.data["token"]).decode("utf-8")
        user = User.objects.get(email=email)
        user.is_active = True
        user.save()
        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(["POST"])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        activation_email.delay(request.data["username"], request.data["email"])

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def login(request):
    username = request.data['username']
    password = request.data['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        refresh = RefreshToken.for_user(user)
        data = {
            'refresh_token': str(refresh),
            'access_token': str(refresh.access_token),
            'id': user.id,
            'username': user.username,
            'email': user.email or None,
            'first_name': user.first_name or None,
            'last_name': user.last_name or None,
            'date_of_birth': user.profile.date_of_birth or None,
            'photo': user.profile.photo or None,
        }
        return Response(data, status=status.HTTP_200_OK)

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def timeline(request):
    user = User.objects.get(username=request.data['username'])
    actions = Action.objects.exclude(user=user)
    following_ids = user.following.values_list('id', flat=True)

    if following_ids:
        actions = actions.filter(user_id__in=following_ids)

    actions = actions.select_related('user', 'user__profile').prefetch_related(
        'target')[:10]

    return Response({'actions': actions})

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def update(request):
    if request.data['key'] == 'date_of_birth':
        Profile.objects.update_or_create(
            user = request.data['id'],
            defaults = {
                request.data['key']: request.data['value']
            },
        )
    else:
        User.objects.update_or_create(
            id = request.data['id'],
            defaults = {
                request.data['key']: request.data['value']
            },
        )
    return Response({
        'data': 'success'
    })
    # user_form = UserEditForm(instance=request.user,data=request.POST)
    # profile_form = ProfileEditForm(instance=request.user.profile,
    #                             data=request.POST, files=request.FILES)
    
    # if user_form.is_valid() and profile_form.is_valid():
    #     user_form.save()
    #     profile_form.save()

## REPLACE
# @login_required
# def dashboard(request):
#     actions = Action.objects.exclude(user=request.user)
#     following_ids = request.user.following.values_list('id', flat=True)

#     if following_ids:
#         actions = actions.filter(user_id__in=following_ids)
#         # второй аргумент должен быть user__profile
#     actions = actions.select_related('user', 'user').prefetch_related(
#         'target')[:10]

#     # Create profile for users created not with register form
#     Profile.objects.get_or_create(user=request.user)

#     return render(request, 'account/dashboard.html',
#                   {'section': 'dashboard', 'actions': actions})

@login_required
def user_list(request):
    """ Список всех активных пользователей. """
    users = User.objects.filter(is_active=True)
    return render(request, 'account/user/list.html',
                  {'section': 'people', 'users': users})


@login_required
def user_detail(request, username):
    user = get_object_or_404(User, username=username, is_active=True)
    return render(request, 'account/user/detail.html',
                  {'section': 'people', 'user': user})

@ajax_required
@require_POST
@login_required
def user_follow(request):
    """
    Ajax-обработчик добавляет и удаляет пользователей из подписок.
    """
    user_id = request.POST.get('id')
    action = request.POST.get('action')
    if user_id in action:
        try:
            user = User.objects.get(id=user_id)
            if action == 'follow':
                Contact.objects.get_or_create(user_from=request.user,
                                              user_to=user)
                create_action(request.user, 'is following', user)
            else:
                Contact.objects.filter(user_from=request.user,
                                       user_to=user).delete()
            return JsonResponse({'status': 'ok'})
        except User.DoesNotExist:
            return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'ok'})

# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             # Создаем нового пользователя, но пока не сохраняем в базу данных.
#             new_user = form.save(commit=False)
#             # Задаем пользователю зашифрованный пароль.
#             new_user.set_password(form.cleaned_data['password'])
#             # Сохраняем пользователя в базе данных.
#             new_user.save()
#             Profile.objects.create(user=new_user)
#             create_action(new_user, 'has created an account')
#             return render(request, 'account/register_done.html',
#                           {'new_user': new_user})
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'account/register.html', {'form': form})

# @login_required
# def edit(request):
#     if request.method == 'POST':
#         user_form = UserEditForm(instance=request.user,data=request.POST)
#         profile_form = ProfileEditForm(instance=request.user.profile,
#                                     data=request.POST, files=request.FILES)
        
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#     else:
#         user_form = UserEditForm(instance=request.user)
#         profile_form = ProfileEditForm(instance=request.user.profile)
#     return render(request,'account/edit.html', {'user_form': user_form,
#                                                 'profile_form': profile_form})
