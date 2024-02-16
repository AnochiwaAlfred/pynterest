from django.contrib import admin
from django.urls import re_path as url
from django.views.static import serve
from django.conf import settings
from django.urls import path, include
from django.conf import settings
from pyns import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:pagename>', views.index, name='index'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('register/', views.registerView, name='register'),
    path('add/', views.addPyn, name='add'),
    path('user/<int:id>/', views.userPyns, name='user_pyns'),
    path('user/<int:id>/saved', views.userSavedPyns, name='saved_pyns'),
    path('user/<int:id>/liked', views.userLikedPyns, name='liked_pyns'),
    path('save/<uuid:id>/', views.savePyn, name='save_pyn'),
    path('remove/<uuid:id>/', views.removePyn, name='remove_pyn'),
    path('like/<uuid:id>/', views.likePyn, name='like_pyn'),
]
