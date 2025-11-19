from django.urls import path
from django.contrib import admin

from . import views
urlpatterns = [
    path('analysis_home/', views.analysis_home1),
    path('a_register1/', views.a_register1),
    path('a_login1/', views.a_login1),
    path('production_details_n3/', views.production_details_n3),
    path('production2/', views.production2),
    # path('send_button/<int:id>/', views.send_button),
    path('production_details_n4/', views.production_details_n4),
    path('get_input/<int:id>/', views.get_input),
    path('production_details_n5/', views.production_details_n5),

]