from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['username','first_name','date','symptoms']

from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['username', 'date', 'first_name', 'symptoms']
        widgets = {
            'date': forms.SelectDateWidget(years=range(2024, 2031)),  # Adjust years as needed
        }

# forms.py
from django import forms
from .models import Rescheduling


class RescheduleForm(forms.ModelForm):
    class Meta:
        model = Rescheduling
        fields = ['PrevSchedule_Time', 'NewSchedule_time', 'Doctor_dep']  # Only allow these fields for rescheduling

    # Adding validation or customizations, if needed
    def clean(self):
        cleaned_data = super().clean()
        prev_schedule = cleaned_data.get("PrevSchedule_Time")
        new_schedule = cleaned_data.get("NewSchedule_time")

        if new_schedule and new_schedule <= prev_schedule:
            raise forms.ValidationError("The new schedule must be after the previous schedule.")

        return cleaned_data

from django import forms
from .models import MedicalR

class MedicalRecordForm(forms.ModelForm):
    class Meta:
        model = MedicalR
        fields = ['patient_name','diagnosis', 'treatment','record_date']