from django.urls import path
from django.contrib import admin

from . import views
urlpatterns = [
    path('quality/', views.quality_home),
    # path('qlogin/', views.qlogin),
    path('register/', views.register),
    path('qlogin1/', views.qlogin1),
    path('raw_materials_2/', views.rawmaterials2),
    path('quality_team_2/', views.quality_team_2),


]