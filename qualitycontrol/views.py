from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
def quality_home(request):
    return render(request, 'quality/qualitycontrol.html')
def register(request):
    if request.method == 'POST':
        print('1')
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        phonenumber = request.POST['phonenumber']
        gender = request.POST['gender']
        address = request.POST['address']
        quality_model1(username=username, password=password, email=email, phonenumber=phonenumber, gender=gender,
                       address=address).save()
        messages.info(request, "registered successfully")
        return redirect('/qlogin1/')
    return render(request, 'quality/quality_login.html')

def qlogin1(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(password)
        print(email)
        try:
            quality_model1.objects.get(email=email, password=password)
            messages.info(request, "login successfully")
            return redirect('/quality/')
        except:
            pass
    return render(request, 'quality/quality_login.html')


def rawmaterials2(request):
    if request.method == 'POST':
        print('1')
        iron_ore = request.POST['iron_ore']
        coking_coal = request.POST['coking_coal']
        ferrous_scrap = request.POST['ferrous_scrap']
        manganese = request.POST['manganese']
        siliconferro_alloy = request.POST['siliconferro_alloy']
        chromium = request.POST['chromium']
        nickel = request.POST['nickel']
        zinc = request.POST['zinc']
        tin = request.POST['tin']
        molybdenum = request.POST['molybdenum']
        vanadium = request.POST['vanadium']
        TUNGSTEN = request.POST['TUNGSTEN']
        raw_materials(iron_ore=iron_ore, coking_coal=coking_coal, ferrous_scrap=ferrous_scrap, manganese=manganese,
                      siliconferro_alloy=siliconferro_alloy,
                      chromium=chromium, nickel=nickel, zinc=zinc, tin=tin, molybdenum=molybdenum, vanadium=vanadium,
                      TUNGSTEN=TUNGSTEN, ).save()
        messages.info(request, "Uploaded successfully")
        return redirect('/quality/')
    return render(request, 'quality/raw_materials.html')


# def quality_team(request):
#     return render(request, 'quality/quality_team.html')


def quality_team_2(request):
    if request.method == 'POST':
        print('1')
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        employee_id = request.POST['employee_id']
        Supplier = request.POST['Supplier']
        inspection_team_type = request.POST['inspection_team_type']
        raw_material_quality = request.POST['raw_material_quality']
        quality_team(name=name, email=email, address=address, employee_id=employee_id,
                     Supplier=Supplier,
                     inspection_team_type=inspection_team_type, raw_material_quality=raw_material_quality).save()
        messages.info(request, "submitted successfully")
        return redirect('/quality/')
    return render(request, 'quality/quality_team.html')
