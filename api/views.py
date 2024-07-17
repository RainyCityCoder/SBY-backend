from django.shortcuts import render
from rest_framework import generics
from .models import Biologists, ComputerScientists
from .serializers import ReplySerializer

# Create your views here.
class Biologists(generics.ListCreateAPIView):
    queryset = Biologists.objects.all().order_by('birthyear')
    serializer_class = ReplySerializer

class ComputerScientists(generics.ListCreateAPIView):
    queryset = ComputerScientists.objects.all().order_by('birthyear')
    serializer_class = ReplySerializer