import json

from django.http import JsonResponse
from .models import UserReg
from django.views.decorators.csrf import csrf_exempt


def registeration(request):
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
            return JsonResponse({"message": "Data saved sucessfully", 'register': user_data.name})

    except Exception as e:
        return JsonResponse({"message": str(e)})


# Create your views here.

def login(request):
    s = json.loads(request.body)
    try:
        data = s.get('name')
        data2 = s.get('password')
        ret = UserReg.objects.filter(name=data, password=data2).first()
        if ret is not None:
            return JsonResponse({"message": "User LoggedIn successfully", 'name': ret.name, "password": ret.password})
        else:
            return JsonResponse({"message": "invalid credentails"})
    except Exception as e:
        return JsonResponse({"message": str(e)})
