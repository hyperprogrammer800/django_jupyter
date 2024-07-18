from django.shortcuts import render
from Task.models import Patient

# Create your views here.
def home(request):
    errors_counts = {
            'Total' : Patient.objects.all().count() ,
            'First name' : Patient.objects.filter(first_name= None).count() ,
            'Last name' : Patient.objects.filter(last_name= None).count() ,
            'MRN' : Patient.objects.filter(mrn= None).count() ,
            'DOB' : Patient.objects.filter(dob= None).count() ,
            'address' : Patient.objects.filter(address= None).count() ,
            'sex' : Patient.objects.filter(sex= None).count() ,
            'phone' : Patient.objects.filter(phone= None).count() ,
            'physician' : Patient.objects.filter(physician= None).count() ,
    }
    context = {
        'errors_counts': errors_counts
    }
    print(Patient.objects.filter(first_name= None).count())
    print(Patient.objects.filter(last_name= None).count())
    print(Patient.objects.filter(dob= None).count())
    print(Patient.objects.filter(mrn= None).count())
    print(Patient.objects.filter(address= None).count())
    print(Patient.objects.filter(physician= None).count())
    print(Patient.objects.filter(phone= None).count())
    print(Patient.objects.filter(sex= None).count())
    print(Patient.objects.all().count())
    return render(request, "Task/home.html", context)