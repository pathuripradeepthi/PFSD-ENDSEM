from django.shortcuts import render

# Create your views here.

def Shomepage(request):
    return render(request,'userapp/Shomepage.html')

# def Book_apointment(request):
#     return render(request,'userapp/Book_apointment.html')





from django.shortcuts import render, redirect
from .forms import AppointmentForm

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()  # Save the appointment to the database
            return redirect('userapp:appointment_success')  # Redirect after successful form submission
    else:
        form = AppointmentForm()

    return render(request, 'userapp/Book_apointment.html', {'form': form})

def appointment_success(request):
    return render(request, 'userapp/appointment_success.html')

from django.shortcuts import render, get_object_or_404, redirect
from .models import Rescheduling
from .forms import RescheduleForm ,AppointmentForm
from django.contrib import messages

def reshedule_app(request):
    if request.method == 'POST':
        form = RescheduleForm(request.POST)
        if form.is_valid():
            form.save()  # Save the appointment to the database
            return redirect('userapp:appointment_success')  # Redirect after successful form submission
    else:
        form = RescheduleForm()

    return render(request, 'userapp/Reschedule_appointment.html', {'form': form})

from django.shortcuts import render
from .models import Appointment

def display_appointments(request):
    # Retrieve all appointments from the database
    appointments = Appointment.objects.all()
    context = {
        'appointments': appointments
    }
    return render(request, 'userapp/display_appointments.html', context)

from django.shortcuts import render

def symptom_checker(request):
    result = None  # Initialize result for displaying diagnosis

    if request.method == "POST":
        # Get the form data directly from the POST request
        symptoms = request.POST.get('symptoms', '')
        duration = request.POST.get('duration', '')
        severity = request.POST.get('severity', '')
        age = request.POST.get('age', '')
        gender = request.POST.get('gender', '')

        # Check if the fields are filled out
        if symptoms and duration and severity and age and gender:
            # Hardcoded result indicating "High fever" diagnosis based on input
            result = (
                f"You have High Fever with the symptoms: {symptoms}.<br>"
                "<strong>Ayurvedic Medicines:</strong> <br>"
                "1. Tulsi (Holy Basil) Tea<br>"
                "2. Ginger and Honey<br>"
                "3. Turmeric Milk<br>"
                "<strong>English Medicines:</strong> <br>"
                "1. Paracetamol<br>"
                "2. Ibuprofen<br>"
                "3. Antibiotics (prescribed by a doctor)"
            )
        else:
            result = "Please fill out all fields."

    return render(request, "userapp/symptom_checker.html", {"result": result})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import MedicalR
from .forms import MedicalRecordForm

def add_medical_record(request):
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userapp:appointment_success')  # Redirect to the record list page
    else:
        form = MedicalRecordForm()
    return render(request, 'userapp/add_medical_record.html', {'form': form})

from django.shortcuts import render
from .models import MedicalR
def view_medical_records(request):
    records = MedicalR.objects.all()
    context = {
        'records':records
    }
    return render(request, 'userapp/view_medical_records.html', context)

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import MedicalR
from .forms import MedicalRecordForm

def add_medical_record(request):
    if request.method == 'POST':
        form = MedicalRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userapp:appointment_success')  # Redirect to the record list page
    else:
        form = MedicalRecordForm()
    return render(request, 'userapp/add_medical_record.html', {'form': form})

from django.shortcuts import render
from .models import MedicalR
def view_medical_records(request):
    records = MedicalR.objects.all()
    context = {
        'records':records
    }
    return render(request, 'userapp/view_medical_records.html', context)