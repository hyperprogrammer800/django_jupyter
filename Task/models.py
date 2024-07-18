from django.db import models

# Create your models here.

class Patient(models.Model):
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    mrn = models.CharField(max_length=20, null=True, blank=True)
    physician = models.CharField(max_length=30, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    address = models.CharField(max_length=80, null=True, blank=True)
    sex = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')), null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"