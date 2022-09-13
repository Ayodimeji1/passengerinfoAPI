from django.db import models

# Create your models here.


class Passenger(models.Model):
    name = models.CharFields(max_length=100)
    age = models.IntergerField(max_digits=3)
    sex = models.

    def __init__(self, arg):
        super(, self).__init__()
        self.arg = arg
