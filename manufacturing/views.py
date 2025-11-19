from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from qualitycontrol.models import *
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
# from sklearn.svm import SVC
from sklearn.ensemble import BaggingClassifier

import warnings

warnings.filterwarnings('ignore')


def manufacturing_home(request):
    return render(request, 'manufacturing/manufacture_home.html')


def mregister1(request):
    if request.method == 'POST':
        print('1')
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        gender = request.POST['gender']
        address = request.POST['address']
        manufacturing_model1(username=username, password=password, email=email, phonenumber=phonenumber, gender=gender,
                             address=address).save()
        messages.info(request, "registered successfully")
        return redirect('/mlogin1/')
    return render(request, 'manufacturing/manufacturing_login.html')


def mlogin1(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(password)
        print(email)
        try:
            manufacturing_model1.objects.get(email=email, password=password)
            messages.info(request, "login successfully")
            return redirect('/manufacture_home/')
        except:
            pass
    return render(request, 'manufacturing/manufacturing_login.html')


def stock_details(request):
    datas = raw_materials.objects.all()
    return render(request, "manufacturing/view_stock_materials.html", {"datas": datas})


# def mprocess(request):
#     return render(request, 'manufacturing/process.html')


def manufacturing_process_1(request):
    if request.method == 'POST':
        print('1')
        iron_making = request.POST['iron_making']
        primary_steel_making = request.POST['primary_steel_making']
        secondary_steel_making = request.POST['secondary_steel_making']
        casting = request.POST['casting']
        first_forming = request.POST['first_forming']
        fabrication = request.POST['fabrication']
        finishing = request.POST['finishing']
        manufacturing_process(iron_making=iron_making, primary_steel_making=primary_steel_making,
                              secondary_steel_making=secondary_steel_making,
                              casting=casting, first_forming=first_forming,
                              fabrication=fabrication, finishing=finishing).save()
        messages.info(request, "submitted successfully")
        return redirect('/manufacture_home/')
    return render(request, 'manufacturing/process.html')


# def output_1(request):
#     return render(request, 'manufacturing/expected_ot.html')


def ex_ot(request):
    if request.method == 'POST':
        print('1')
        iron_ore = request.POST['iron_ore']
        COKING_COAL = request.POST['COKING_COAL']
        FERROUS_SCRAP = request.POST['FERROUS_SCRAP']
        METHOD = request.POST['METHOD']
        expected_ot(iron_ore=iron_ore, COKING_COAL=COKING_COAL,
                    FERROUS_SCRAP=FERROUS_SCRAP,
                    METHOD=METHOD).save()
        messages.info(request, "submitted successfully")
        return redirect('/manufacture_home/')
    return render(request, 'manufacturing/expected_ot.html')


def ot_prediction(request, id):
    get = expected_ot.objects.get(id=id)
    r = get.id
    a = get.iron_ore
    b = get.COKING_COAL
    c = get.FERROUS_SCRAP
    d = get.METHOD

    if d == "Basic Oxygen Furnace - BOF":
        e = (int(a) + int(b) + int(c)) * 80 / 100
        print(a + b + c)
        print("Expected Liquid Steel", e, "Kgs")
        get.OUTPUT = e
        get.save()
        # add=a+b+c
        # waste=add-e
        # print("Expexted Waste",waste)
        messages.info(request, "successfully completed")
        return redirect('/predict_1/')

    else:
        f = (int(a) + int(b) + int(c)) * 60 / 100
        print(a + b + c)
        print("Expected Liquid Steel", f, 'Kgs')
        get.OUTPUT = f
        get.save()
        # add1 = a + b + c
        # waste1 = add1 - f
        # print("Expexted Waste", waste1)
        messages.info(request, "successfully completed")
        return redirect('/predict_1/')


def predict_1(request):
    datas = expected_ot.objects.all()
    return render(request, "manufacturing/predict.html", {"datas": datas})
