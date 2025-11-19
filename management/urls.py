from django.urls import path
from django.contrib import admin

from . import views
urlpatterns = [
    path('management_home/', views.management_home_1),
    path('m2_register1/', views.m2_register1),
    path('m2_login1/', views.m2_login1),
    path('production_1/', views.production_1),
    path('expected_3/', views.expected_3),
    path('ot_prediction_2/', views.ot_prediction_2),
    path('waste_out/<int:id>/', views.waste_out),



]