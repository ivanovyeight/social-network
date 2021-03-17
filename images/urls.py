from django.urls import path
from . import views


urlpatterns = [
    path('ranking/', views.image_ranking, name='ranking'),
    path('like/', views.image_like, name='image_like'),
    path('', views.image_list, name='list'),

    #api
    path('api/create/', views.image_create, name='image_create'),
    path('api/detail/<int:id>/<slug:slug>/', views.image_detail, name='detail'),

]
