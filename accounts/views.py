from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from django.core.serializers import serialize
from django.core.exceptions import ValidationError, ObjectDoesNotExist
from http import HTTPStatus
import re
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


@method_decorator(csrf_exempt, name="dispatch")
class RegisterAPIView(View):

    def post(self, request):
        allowed_parameters = {"email", "password1", "password2"}
        request_data = json.loads(request.body)
        for key in request_data:
            if key not in allowed_parameters:
                return JsonResponse({"status": "error",
                                     "error_message": "Extra parameters are not allowed"},
                                    status=HTTPStatus.BAD_REQUEST)
        email = request_data.get("email")
        password1 = request_data.get("password1")
        password2 = request_data.get("password2")

        if re.fullmatch(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b", email):
            try:
                if validate_password(password1) is None:
                    if password1 == password2:

                        user = User.objects.create(**{"email": email, "password": password1})
                        user.save()
                        return JsonResponse({"status": "success",
                                             "email": email},
                                            status=HTTPStatus.CREATED)
                    return JsonResponse({"status": "error",
                                         "error_message": "Passwords mismatch"},
                                          status=HTTPStatus.BAD_REQUEST)
            except ValidationError as error:
                return JsonResponse({"status": "error",
                                     "error_message": "".join(error)},
                                    status=HTTPStatus.BAD_REQUEST)


@method_decorator(csrf_exempt, name="dispatch")
class ResetPasswordAPIView(View):

    def put(self, request, user_id):
        request_data = json.loads(request.body)
        request_token = request_data.get("token")
        new_password1 = request_data.get("new_password1")
        new_password2 = request_data.get("new_password2")
        try:
            user = User.objects.get(id=user_id)
            user_token = user.token
            if request_token != user_token:
                return JsonResponse({"status": "error",
                                     "message": "Invalid token was provided"},
                                    status=HTTPStatus.BAD_REQUEST)
            try:
                if validate_password(new_password1) is None:
                    if new_password1 == new_password2:
                        user.password = new_password1
                        user.save()
                        return JsonResponse({"status": "succes",
                                             "message": "Password was successfully changed"},
                                            status=HTTPStatus.OK)
                    return JsonResponse({"status": "error",
                                         "message": "Passwords are not equal to each other"},
                                        status=HTTPStatus.BAD_REQUEST)
            except ValidationError as error:
                return JsonResponse({"status": "error",
                                     "message": "".join(error)},
                                    status=HTTPStatus.BAD_REQUEST)
        except ObjectDoesNotExist as error:
            return JsonResponse({"status": "error",
                                 "message": f"{error}"},
                                 status=HTTPStatus.BAD_REQUEST)









