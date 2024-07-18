from django.test import TestCase

# Create your tests here.
from Task.models import Patient

print(Patient.objects.all())