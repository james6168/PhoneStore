from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from django.core.serializers import serialize
from http import HTTPStatus
from django.contrib.auth import authenticate
import json
# Create your views here.

User = get_user_model()


@method_decorator(csrf_exempt, name="dispatch")
class LoginAPIView(View):

    def post(self, request):
        request_data = json.loads(request.body)
        user = User.objects.filter(email=request_data.get("email"))
        if user:
            if user[0].check_password(request_data.get("password")):
                user_token = serialize("python", user)[0].get("fields").get("token")

                response_data = {
                    "token": user_token
                }
                return JsonResponse(response_data, status=HTTPStatus.OK)
            return JsonResponse({"error": "Incorrect password"}, status=HTTPStatus.BAD_REQUEST)
        return JsonResponse({"error": "Such user does not exist"}, status=HTTPStatus.BAD_REQUEST)


