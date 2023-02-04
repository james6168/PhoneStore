from django.urls import path
from accounts.views import *
urlpatterns = [
    path('accounts/login/', LoginAPIView.as_view()),
    path('accounts/register/', RegisterAPIView.as_view())
]