from django.urls import path
from accounts.views import LoginAPIView
urlpatterns = [
    path('accounts/login/', LoginAPIView.as_view())
]