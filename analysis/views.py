from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from manufacturing.models import *
from management.models import *
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
# from sklearn.svm import SVC
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import warnings
warnings.filterwarnings('ignore')
def analysis_home1(request):
    return render(request, 'analysis/analysis_home.html')

def a_register1(request):
    if request.method == 'POST':
        print('1')
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        gender = request.POST['gender']
        address = request.POST['address']
        analysis_model1(username=username, password=password, email=email, phonenumber=phonenumber, gender=gender,
                        address=address).save()
        messages.info(request, "registered successfully")
        return redirect('/a_login1/')
    return render(request, 'analysis/analysis_login.html')

def a_login1(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(password)
        print(email)
        try:
            analysis_model1.objects.get(email=email, password=password)
            messages.info(request, "login successfully")
            return redirect('/analysis_home/')
        except:
            pass
    return render(request, 'analysis/analysis_login.html')


def production_details_n3(request):
    datas = manufacturing_process.objects.all()
    return render(request, "analysis/production_details_3.html", {"datas": datas})


def production2(request):
    datas = expected_ot.objects.all()
    return render(request, "analysis/production_2.html", {"datas": datas})


def manufacturing_procecsssss(request):
    datas = manufacturing_process.objects.filter(approve=False,final__isnull =True)
    return render(request, "manufacturing/test.html", {"datas": datas})


def algo(datas,r):

    print(datas)

    data = pd.read_csv('test1.csv')
    data_x = data.iloc[:, :-1]
    data_y = data.iloc[:, -1]
    string_datas = [i for i in data_x.columns if data_x.dtypes[i] == np.object_]

    LabelEncoders = []
    for i in string_datas:
        newLabelEncoder = LabelEncoder()
        data_x[i] = newLabelEncoder.fit_transform(data_x[i])
        LabelEncoders.append(newLabelEncoder)
    ylabel_encoder = None
    if type(data_y.iloc[1]) == str:
        ylabel_encoder = LabelEncoder()
        data_y = ylabel_encoder.fit_transform(data_y)

    model = LinearDiscriminantAnalysis()
    model.fit(data_x, data_y)

    value = {data_x.columns[i]: datas[i] for i in range(len(datas))}
    l = 0
    for i in string_datas:
        z = LabelEncoders[l]
        value[i] = z.transform([value[i]])[0]
        l += 1
    value = [i for i in value.values()]
    predicted = model.predict([value])

    if ylabel_encoder:
        predicted = ylabel_encoder.inverse_transform(predicted)
    return predicted[0]


def get_input(request, id):
    get = manufacturing_process.objects.get(id=id)
    r = get.id
    inputvar = []
    get.save()

    a = get.primary_steel_making
    b = get.secondary_steel_making
    c = get.casting
    d = get.finishing

    print(a)
    print(b)

    inputvar.append(a)
    inputvar.append(d)
    inputvar.append(c)
    inputvar.append(b)
    print('input:', inputvar)
    f = algo(inputvar, r)
    print('OUTPUT:', f)
    st = manufacturing_process.objects.filter(id=r).update(final=f)
    return redirect('/production_details_n5/')


# def send_button(request, id):
#     datas = manufacturing_process.objects.get(id=id)
#     datas.approve = True
#     datas.save()
#     print('hi')
#     messages.info(request, "successfully sent")
#     return redirect('/management_verify/')


def production_details_n4(request):
    datas = manufacturing_process.objects.all()
    return render(request, "analysis/managing.html", {"datas": datas})


def production_details_n5(request):
    datas = manufacturing_process.objects.all()
    return render(request, "analysis/waste_2.html", {"datas": datas})