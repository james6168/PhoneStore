from django.urls import path
from smartphones.views import *

urlpatterns = [
    path("list/", SmartphoneListAPIView.as_view())
]