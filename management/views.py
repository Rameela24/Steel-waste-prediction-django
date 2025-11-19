from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from manufacturing.models import *
def management_home_1(request):
    return render(request, 'management/home.html')
def m2_register1(request):
    if request.method == 'POST':
        print('1')
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        gender = request.POST['gender']
        address = request.POST['address']
        management_model1(username=username, password=password, email=email, phonenumber=phonenumber, gender=gender,
                          address=address).save()
        messages.info(request, "registered successfully")
        return redirect('/m2_login1/')
    return render(request, 'management/management_login.html')
def m2_login1(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(password)
        print(email)
        try:
            management_model1.objects.get(email=email, password=password)
            messages.info(request, "login successfully")
            return redirect('/management_home/')
        except:
            pass
    return render(request, 'management/management_login.html')


def production_1(request):
    datas = manufacturing_process.objects.all()
    return render(request, "management/production_details.html", {"datas": datas})

def expected_3(request):
    datas = expected_ot.objects.all()
    return render(request, "management/expected_output.html", {"datas": datas})

def waste_out(request,id):
    print("hi",id)
    get = expected_ot.objects.get(id=id)
    r = get.id
    a = get.iron_ore
    b = get.COKING_COAL
    c = get.FERROUS_SCRAP
    d = get.METHOD

    if d=="Basic Oxygen Furnace - BOF":
        e = (int(a) +int(b) + int(c)) * 80 / 100
        # print(a + b + c)
        # print("Expected Liquid Steel",e,"Kgs")
        add = int(a) + int(b) + int(c)
        waste = int(add) - int(e)
        get.WASTE = waste
        get.save()

        messages.info(request, "successfully completed")
        return redirect('/ot_prediction_2/')

    else:
        f = (int(a) +int(b)  + int(c)) * 60 / 100
        # print(a + b + c)
        # print("Expected Liquid Steel",f,'Kgs')
        add1 = int(a) + int(b) + int(c)
        waste1 = int(add1) - int(f)

        get.WASTE = waste1
        get.save()

        messages.info(request, "successfully completed")
        return redirect('/ot_prediction_2/')


def ot_prediction_2(request):
    datas = expected_ot.objects.all()
    return render(request,"management/WASTE.html", {"datas": datas})

