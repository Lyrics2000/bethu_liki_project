from os import times
from django.db import models

# Create your models here.
class Passengers(models.Model):
    name =  models.CharField(max_length=255)
    age =  models.IntegerField()
    phone =  models.CharField(max_length=255)
    passport = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Gate(models.Model):
    passenger_id =  models.ForeignKey(Passengers,on_delete=models.CASCADE)
    open =  models.BooleanField(default=False)
    time =  models.DateTimeField()
    
    def __str__(self):
        return str(self.passenger_id)


class Flights(models.Model):
    passenger_id =  models.ForeignKey(Passengers,on_delete=models.CASCADE)
    flight_number  =  models.CharField(max_length=255)
    destination =  models.CharField(max_length=255)
    arrival_time =  models.DateTimeField()

    def __str__(self):
        return str(self.passenger_id)


class Tempereture(models.Model):
    passenger_id =  models.ForeignKey(Passengers,on_delete=models.CASCADE)
    tempereture_value =  models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return str(self.passenger_id)