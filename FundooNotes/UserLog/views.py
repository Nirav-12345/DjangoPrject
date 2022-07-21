import json

from django.http import JsonResponse
from .models import UserReg


def registration(request):
    try:
        # print(request.body)
        data = json.loads(request.body)
        if request.method == 'POST':
            user_data = UserReg(name=data.get('name'),
                                password=data.get('password'),
                                phone_number=data.get('phone_number'),
                                location=data.get('location'),
                                email=data.get('email'))
            user_data.save()
            return JsonResponse({"message": "Data saved sucessfully", "data": {'register': user_data.name}}, status=201)

    except Exception as e:
        return JsonResponse({"message": str(e), "data": {}}, status=400)


# Create your views here.

def login(request):
    raw_data = json.loads(request.body)
    try:
        username = raw_data.get('name')
        password = raw_data.get('password')
        auth_user = UserReg.objects.filter(name=username, password=password).first()
        if auth_user:
            return JsonResponse({"message": "User LoggedIn successfully",
                                 "data": {'name': auth_user.name, "password": auth_user.password}}, status=200)

        return JsonResponse({"message": "invalid credentials", "data": {}}, status=401)
    except Exception as e:
        return JsonResponse({"message": str(e), "data": {}}, status=400)
