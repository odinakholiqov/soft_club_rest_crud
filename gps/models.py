from django.db import models


class Driver(models.Model):
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Vehicle(models.Model):
    BUS = "BS"
    MINIBUS = "MBS"
    TROLLEYBUS = "TBS"
    TRANSPORT_TYPE_CHOICES = [
        (BUS, "Bus"),
        (MINIBUS, "Minibus"),
        (TROLLEYBUS, "Trolleybus"),
    ]
    transport_type = models.CharField(max_length=3, choices=TRANSPORT_TYPE_CHOICES, default=BUS)

    route_number = models.PositiveSmallIntegerField()
    license_number = models.CharField(max_length=8)

    is_active = models.BooleanField(default=True)

    tracker = models.OneToOneField("Tracker", on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"{self.transport_type} ({self.route_number}): {self.license_number}"



class Trip(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.driver}: {self.vehicle} ({self.created_at})"


class Location(models.Model):
    longitude = models.CharField(max_length=8)
    latitude = models.CharField(max_length=8)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.trip}: {self.longitude} (long), {self.latitude} (lati)"


class Tracker(models.Model):
    version = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.version