from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.


class Passenger(models.Model):
    id = models.IntegerField(primary_key=True, validators=[MaxValueValidator(999999999)])
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    departure = models.CharField(max_length=100)
    arrival = models.CharField(max_length=100)

    def __str__(self):
        return self.name+self.age+self.sex
