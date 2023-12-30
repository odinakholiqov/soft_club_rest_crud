
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import CharField
from .models import *


class VehicleSerializer(ModelSerializer):
    class Meta:
        model = Vehicle
        fields = "__all__"


class DriverSerializer(ModelSerializer):
    class Meta:
        model = Driver
        fields = "__all__"


class TripSerializer(ModelSerializer):
    driver = DriverSerializer(read_only=True)
    vehicle = VehicleSerializer(read_only=True)
    class Meta:
        model = Trip
        fields = "__all__"

   

class LocationSerializer(ModelSerializer):
    tracker = CharField(write_only=True)
    trip = TripSerializer(read_only=True)
    
    class Meta:
        model = Location
        fields = ("longitude", "latitude", "trip", "tracker")

    def create(self, validated_data):
        
        tracker = Tracker.objects.filter(version=validated_data["tracker"]).first()    
        vehicle = Vehicle.objects.filter(tracker=tracker).first()
        trip = Trip.objects.filter(vehicle=vehicle).first()

        validated_data["trip"] = trip
        del validated_data["tracker"]
        
        location = Location.objects.create(**validated_data)

        return location