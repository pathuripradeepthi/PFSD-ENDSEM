from django.urls import path, include
from .views import symptom_checker
from . import views
app_name='userapp'
urlpatterns = [
    path('Shomepage/',views.Shomepage,name='Shomepage'),
    path('book_appointment/',views.book_appointment,name='book_appointment'),

    path('appointment_success/', views.appointment_success, name='appointment_success'),
    path('Reschedule_appointment/', views.reshedule_app, name='reschedule_app'),
    path('display_appointments/', views.display_appointments, name='display_appointments'),
    path("symptom-checker/", symptom_checker, name="symptom_checker"),
    path('add_medical_record/', views.add_medical_record, name='add_medical_record'),
    path('view_medical_records/', views.view_medical_records, name='view_medical_records'),


]