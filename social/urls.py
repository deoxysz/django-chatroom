from django.contrib.auth import views as auth_views
from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    
    ## Rooms
    path('room/<str:pk>/', views.room, name="room"),
    path('room-creation/', views.roomCreate, name='roomCreate'),
    path('room-update/<str:pk>/', views.roomEdit, name='roomEdit'),
    path('room-delete/<str:pk>/', views.roomDelete, name='roomDelete'),


    ## Replies
    path('reply-delete/<str:pk>/', views.replyDelete, name="replyDelete"),
    path('reply-edit/<str:pk>/', views.replyEdit, name="replyEdit"),
    
    ## Account
    path('create-account/', views.SignUp.as_view(), name='signUp'),
    path('login/', auth_views.LoginView.as_view(template_name = 'login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]