from django.urls import path
from .views import UserCreateApiView, UserProfileUpdateApiView

urlpatterns = [
  path('users/create/', UserCreateApiView.as_view(), name='create_user'),
  path('users/<int:pk>/update-profile', UserProfileUpdateApiView.as_view(), name='update-profile')
]