from django.views.generic import *
from django.http.response import JsonResponse
from smartphones.models import *
from django.core.serializers import serialize

# Create your views here.


class SmartphoneListAPIView(View):

    def get(self, request):
        smartphones_query_set = serialize("python", Smartphone.objects.all())
        return JsonResponse({"status": "success",
                             "smartphones": smartphones_query_set})


