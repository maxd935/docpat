from django.db import models
from accounts import models as accounts_models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    def __str__(self):
        return self.name

class Appointment(models.Model):
    # PENDING = "pending"
    # CANCELED = "canceled"
    # COMPLETED = "completed"
    # STATUS_CHOICES = [
    #     (PENDING, "Pending"),
    #     (CANCELED, "Canceled"),
    #     (COMPLETED, "Completed"),
    # ]
    doctor = models.ForeignKey(accounts_models.CustomUser, on_delete=models.CASCADE,related_name='doctor')
    patient = models.ForeignKey(accounts_models.CustomUser, on_delete=models.CASCADE,related_name='patient')
    date = models.DateField()
    # status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)
    services = models.ManyToManyField(Service,related_name='appointment_services',default=None)
    # time = models.TimeField()
    def __str__(self):
        return self.doctor.last_name + ' ' + self.patient.last_name

    def get_services(self):
        return ", ".join([service.name for service in self.services.all()])

class Bill(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    def __str__(self):
        return self.appointment.doctor.last_name + ' ' + self.appointment.patient.last_name

class DoctorInfo(models.Model):
    doctor = models.ForeignKey(accounts_models.CustomUser, on_delete=models.CASCADE)
    speciality = models.CharField(max_length=100)
    description = models.TextField()
    services = models.ManyToManyField(Service,related_name='doctor_services',default=None)
    def __str__(self):
        return self.doctor.last_name

    def get_services(self):
        return ", ".join([service.name for service in self.services.all()])
