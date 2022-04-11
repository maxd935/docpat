# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from doctorBackOffice.models import Appointment, Service, DoctorInfo, Bill

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "username", "user_type",
                    "address", "phone", ]


admin.site.register(CustomUser, CustomUserAdmin)
