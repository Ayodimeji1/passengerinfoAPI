from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.


class Passenger(models.Model):
    id = models.IntegerField(primary_key=True, validators=[MaxValueValidator(999999999)])
    name = models.CharField(max_length=100)
    age = models.IntegerField(validators=[MaxValueValidator(99)])
    sex = models.CharField(max_length=10)

    def __str__(self):
        return self.name+self.age+self.sex
