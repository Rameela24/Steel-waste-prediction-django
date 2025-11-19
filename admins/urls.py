from django.urls import path
from django.contrib import admin

from . import views
urlpatterns = [
    path('admin_home/', views.admin_home_1),
    path('admin_login/', views.admin_login),
    path('stock_details_2/', views.stock_details_2),
    path('production_details_2/', views.production_details_2),
    path('analysed_output/', views.analysed_outpt),
    path('Quality_team_1/', views.Quality_team_1)
]