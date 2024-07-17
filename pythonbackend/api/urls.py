from django.urls import path
from . import views

urlpatterns = [
    path('compsci/', 
         views.ComputerScientists.as_view(),
         name='computerscientists'),
    path('bio/', 
         views.Biologists.as_view(), 
         name='biologists')
]