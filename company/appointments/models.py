from django.db import models
from ..people.models import Employee
# Create your models here.
class Appointment(models.Model):
    date = models.DateTimeField()

    _employee = models.ForeignKey(
        to=Employee,
        on_delete=models.CASCADE
    )