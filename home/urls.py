from django.urls import path
from . import views
from cliente import views as lp_v
import os

urlpatterns = [
    path('', views.index, name = "index"),
    path('about/', views.about, name = "about"),
    path('search/', views.search, name = "search"),
    path('landingpage/', lp_v.cliente, name = "cliente")
]

current_directory = os.path.dirname(os.path.abspath(__file__))

image_path = "logos"

image_directory = os.path.join(current_directory,image_path)

logos_paths = []
for filename in os.listdir(image_directory):
    if filename.endswith(".png"):
        logos_paths.append(os.path.join(image_directory,filename))

print(logos_paths)
