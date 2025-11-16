from django.db import models
from django.utils import timezone

from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=255, unique=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10)
    contact = models.CharField(max_length=15, blank=True, null=True)
    medical_history = models.TextField(blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)
    medications = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    doctor = models.CharField(max_length=255)
    reason = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, default='Scheduled')

    def __str__(self):
        return f"{self.patient.name} - {self.date} {self.time}"


class Staff(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    department = models.CharField(max_length=100, blank=True, null=True)
    contact = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    contact = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Prescription(models.Model):
    doctor_name = models.CharField(max_length=100)
    date = models.DateField()
    patient_name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    diagnosis = models.TextField(null=True, blank=True)
    medicine_name = models.CharField(max_length=200)
    dosage = models.CharField(max_length=100)
    frequency = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    remarks = models.TextField(null=True, blank=True)   

    def __str__(self):
        return f"{self.patient_name} - {self.doctor_name}"


class CaseStudy(models.Model):
    patient_name = models.CharField(max_length=100)
    diagnosis = models.TextField()
    treatment = models.TextField()
    outcome = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient_name


class DoctorSchedule(models.Model):
    doctor_name = models.CharField(max_length=100)
    weekday = models.CharField(max_length=20)
    visiting_time = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=[('Active', 'Active'), ('Inactive', 'Inactive')])

    def __str__(self):
        return f"{self.doctor_name} - {self.weekday}"

class PatientSummary(models.Model):
    patient = models.OneToOneField('Patient', on_delete=models.CASCADE)
    diagnosis = models.TextField(blank=True, null=True)
    treatment = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Summary - {self.patient.name}"


class DischargeSummary(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    discharge_date = models.DateField(default=timezone.now)
    condition_on_discharge = models.TextField(blank=True, null=True)
    follow_up_instructions = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Discharge - {self.patient.name}"