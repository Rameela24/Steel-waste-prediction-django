from django.urls import path
from django.contrib import admin

from . import views
urlpatterns = [
    path('manufacture_home/', views.manufacturing_home),
    path('mregister/', views.mregister1),
    path('mlogin1/', views.mlogin1),
    path('stock_details/', views.stock_details),
    path('ex_ot/', views.ex_ot),
    path('manufacturing_process_1/', views.manufacturing_process_1),
    path('predict_1/', views.predict_1),
    path('ot_prediction/<int:id>/', views.ot_prediction),



]