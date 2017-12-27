from django.http import  HttpResponse
from django.http import JsonResponse
import json
import datetime
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from ParkingShare.models import User

"""
@csrf_exempt
def hello(request):
    return HttpResponse("<form action='95.220.71.53:8000/login/' method='POST'><p><label for='number'>Number: </label><input type='text' name='number'></p><input value='TITS' type='submit' /></form>");
"""
@csrf_exempt
def Vremya(request):
    now = datetime.datetime.now()
    response = "Time now is %s" %now
    return HttpResponse(response)

@csrf_exempt
def RegisterUser(request):
    b = json.load(request)
    newUser = User(phoneNumber=b['phoneNumber'], password=b['password'])
    all = User.objects.all()
    for x in all:
        if x.phoneNumber == newUser.phoneNumber:
            print("User with phoneNumber" + newUser.phoneNumber + "already registered")
            return HttpResponse("already exists")

        newUser.save()
        print ("New user registered:")
        print ("phoneNumber:" + newUser.phoneNumber)
        print ("Password:" + newUser.password )
        return HttpResponse("OK!")



@csrf_exempt
def loginUser(request):
    b = json.load(request)
    print("Login:")
    print("PhoneNumber" + b['phoneNumber'])
    print("Password" + b['password'])
    all = User.objects.all()
    for x in all:
        if x.phoneNumber == b['phoneNumber']:
            response = HttpResponse("Success")
            response.set_cookie("phoneNumber",b['phoneNumber'])
            response.set_cookie("password", b['password'])
            print("success")
            return response
    else:
        print("Error")
        return HttpResponse("LoginAborted")

@csrf_exempt
def logautUser(request):
    response = HttpResponse("ok")
    response.set_cookie("phoneNumber", "")
    response.set_cookie("password", "")
    return response


@csrf_exempt
def getData(request):
    if "phoneNumber" not in request.COOKIES or request.COOKIES["phoneNumber"] == "":
        return JsonResponse ({'status':'error'})

    users = User.objects.all()
    for user in users:
        if user.phoneNumber == request.COOKIES["phoneNumber"]:
            return JsonResponse({'status':'ok', 'name':user.name, 'surname':user.surname, 'city':user.city, 'sex':user.sex, 'date_of_birth': user.date_of_birth})

    return JsonResponse({'status':'error'})


@csrf_exempt
def acceptChange(request):
    if "phoneNumber" not in request.COOKIES or request.COOKIES["phoneNumber"] == "":
        return HttpResponse('error')
    users = User.objects.all()
    for user in users:
        if user.phoneNumber in request.COOKIES["phoneNumber"]:
            b = json.load(request)
            user.name = b["name"]
            user.surname = b["surname"]
            user.city = b["city"]
            user.sex = b["sex"]
            user.date_of_birth = b["date_of_birth"]
            user.save()

            return HttpResponse('ok')

        return HttpResponse('error')
