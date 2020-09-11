from django.db import models

# Create your models here.
# This is a place where you are going to define the type of the data
# for the database of your application
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)
    
    def __str__(self):
        return f"{self.city} ({self.code})"

class Flight(models.Model):
    # origin = models.CharField(max_length=64)
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    # destination = models.CharField(max_length=64)
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()

    # __str__ = screen function
    # define what object should look like when its printed out to a screen
    def __str__(self):
        return f"{self.id} - {self.origin} to {self.destination}"

