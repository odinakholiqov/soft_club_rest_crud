from rest_framework import viewsets
from .models import *
from .serializers import *



class VehicleAPI(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class DriverAPI(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class TripAPI(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

    
class LocationAPI(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
