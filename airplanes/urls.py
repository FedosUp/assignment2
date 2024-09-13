
from django.urls import path
from airplanes import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>', views.vehicle_detail, name='vehicle_detail'),
    path('find/', views.vehicle_find_icao24, name='vehicle_find_icao24'),
    path('find_country/', views.vehicle_find_origin_country, name='vehicle_find_origin_country'),

]