from django.shortcuts import render, redirect
from .models import *
from qualitycontrol.models import *
from manufacturing.models import *
from django.contrib import messages

def admin_home_1(request):
    return render(request, 'admin/admin_home.html')

def stock_details_2(request):
    datas = raw_materials.objects.all()
    return render(request, "admin/view_stock_materials2.html", {"datas": datas})

def production_details_2(request):
    datas = manufacturing_process.objects.all()
    return render(request, "admin/production_details_2.html", {"datas": datas})

def admin_login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        # print(email)
        if email == "admin@gmail.com" and password == "admin":
            # print(email)
            request.session['admin'] = "admin@gmail.com"
            messages.info(request, "login successfully")
            return render(request, 'admin/admin_home.html')
        elif email != "admin@gmail.com":
            messages.error(request, "Wrong Mail id")
            return render(request, 'admin/adminlogin.html')
        elif password != "admin":
            messages.error(request, "wrong password")
            return render(request, 'admin/adminlogin.html')
        else:
            return render(request, 'admin/adminlogin.html')
    return render(request, 'admin/adminlogin.html')

def analysed_outpt(request):
    datas = expected_ot.objects.all()
    return render(request, "admin/output_waste.html", {"datas": datas})

def Quality_team_1(request):
    datas = quality_team.objects.all()
    return render(request, "admin/Quality Team details.html", {"datas": datas})
