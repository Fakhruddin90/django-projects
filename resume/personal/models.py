from django.db import models

# Create your models here.
class Personal(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    email = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.first_name} {self.last_name} " + ": " + f"{self.email}"