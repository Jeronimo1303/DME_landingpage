from django.urls import path
from . import views
from cliente import views as lp_v

urlpatterns = [
    path('', views.index, name = "index"),
    path('about/', views.about, name = "about"),
    path('search/', views.search, name = "search"),
    path('landingpage/', lp_v.cliente, name = "cliente")
]