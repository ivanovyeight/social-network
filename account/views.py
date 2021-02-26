from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from . forms import LoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    return render(request,'account/dashboard.html',{'section': 'dashboard'})


@login_required
def user_list(request):
    """ Список всех активных пользователей. """
    users = User.objects.filter(is_active=True)
    return render(request, '', {'section': 'people', 'users': users})


@login_required
def user_detail(request, username):
    user = get_object_or_404(User, username=username, is_active=True)
    return render(request, '', {'section': 'people', 'user': user})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Создаем нового пользователя, но пока не сохраняем в базу данных.
            new_user = form.save(commit=False)
            # Задаем пользователю зашифрованный пароль.
            new_user.set_password(form.cleaned_data['password'])
            # Сохраняем пользователя в базе данных.
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        form = UserRegistrationForm()
    return render(request,'account/register.html',{'form': form})


# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'], password=cd['password'])
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponse('Authenticated successfully')
#             else:
#                 return HttpResponse('Disabled account')
#         else:
#             return HttpResponse('Invalid login')
#     else:
#         form = LoginForm()
#     return render(request, 'account/login.html', {'form': form})
