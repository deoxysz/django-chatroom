from django.urls import path

from . import views

urlpatterns = [
    path('', views.getRoutes, name='api'),
    path('rooms/', views.apiRooms),
    path('rooms/<str:pk>/', views.specificRoom),
    path('addroom/', views.RoomAPIView.as_view())
]