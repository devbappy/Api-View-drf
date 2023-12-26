from django.shortcuts import render
from rest_framework import generics

from .models import Location, Item
from .serializers import LocationSerializer, ItemSerializer

import requests

# Create your views here.

# def home(request):
#     response=Item.objects.all()
#     return render(request, 'home.html', {'response':response})



class ItemList(generics.ListCreateAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(location=location)
        return queryset


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
