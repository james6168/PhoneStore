from django.urls import path
from accounts.views import *
urlpatterns = [
    path('login/', LoginAPIView.as_view()),
    path('register/', RegisterAPIView.as_view()),
    path('reset-password/<int:user_id>/', ResetPasswordAPIView.as_view()),
    path('delete-user/<int:user_id>/', DeleteUserAPIView.as_view())
]