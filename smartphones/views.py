from django.views.generic import *
from django.http.response import JsonResponse
from smartphones.models import *
from django.core.serializers import serialize
from http import HTTPStatus
from django.db.models import Q

# Create your views here.


class SmartphoneListAPIView(View):
    global allowed_parameters
    allowed_parameters = {"page", "search"}

    def get(self, request):
        query_dict = request.GET
        search_parameter = query_dict.get("search")
        page_parameter = int(query_dict.get("page"))
        for each_key in query_dict:
            if each_key not in allowed_parameters:
                return JsonResponse({"status": "error",
                                     "message": "Extra keys are not allowed"},
                                    status=HTTPStatus.BAD_REQUEST)

        smartphones_query_set = Smartphone.objects.all()

        if query_dict.get("search") == None:
            elements_sublists = [smartphones_query_set[x: x + 2] for x in range(0, len(smartphones_query_set), 2)]
            pages_count = len(elements_sublists)
            print(elements_sublists)
            print(page_parameter)

            if page_parameter is not None:
                return JsonResponse({"status": "success",
                                     "smartphones": serialize("python", elements_sublists[page_parameter])},
                                    status=HTTPStatus.OK)

            return JsonResponse({"status": "success",
                                 "smartphones": serialize("python", smartphones_query_set)},
                                 status=HTTPStatus.OK)
        else:
            smartphones_query_set = smartphones_query_set.filter(Q(name__icontains=search_parameter) | Q(description__icontains=search_parameter))
            return JsonResponse({"status": "success",
                                 "smartphones": serialize("python", smartphones_query_set)},
                                status=HTTPStatus.OK)

