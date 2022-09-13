from django.db import models

# Create your models here.


class Passenger(models.Model):
    id = models.IntergerField(max_length=100)
    name = models.CharField(max_length=100)
    age = models.IntergerField(max_digits=3)
    sex = models.CharField(max_length=10)

    def __str__(self):
        return self.name+self.age+self.sex
