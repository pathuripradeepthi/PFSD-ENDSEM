from django.db import models

# Create your models here.
from django.db import models

class Book(models.Model):
    username = models.CharField(max_length=10)
    date = models.DateField()
    first_name = models.CharField(max_length=20)
    symptoms = models.CharField(max_length=200)

    def str(self):
        return f"{self.first_name} {self.username} {self.date} {self.symptoms}"

from django.db import models

class Appointment(models.Model):
    username = models.CharField(max_length=10)
    date = models.DateField()
    first_name = models.CharField(max_length=20)
    symptoms = models.CharField(max_length=200)

    def str(self):
        return f"{self.first_name} {self.username} {self.date} {self.symptoms}"
class Rescheduling(models.Model):
    name = models.CharField(max_length=30)
    PrevSchedule_Time = models.DateTimeField()
    NewSchedule_time = models.DateTimeField(null=True, blank=True)
    Doctor_dep = models.CharField(max_length=30)

    def _str_(self):
        return f"{self.name} {self.PrevSchedule_Time} {self.NewSchedule_time} {self.Doctor_dep}"


from django.db import models

class MedicalR(models.Model):
    patient_name = models.CharField(max_length=100)  # Link to the patient (assuming you use Django's User model)
    diagnosis = models.TextField()  # Diagnosis details
    treatment = models.TextField()  # Treatment details
    record_date = models.DateField()  # Date of record creation

    def str(self):
        return f"{self.patient_name} {self.diagnosis} {self.treatment} {self.record_date}"