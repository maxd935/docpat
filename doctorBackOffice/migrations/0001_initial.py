# Generated by Django 3.1.1 on 2022-04-12 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.IntegerField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to=settings.AUTH_USER_MODEL)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DoctorInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('speciality', models.CharField(choices=[('allergists', 'Allergists'), ('diabetologist', 'Diabetologist'), ('dermatologist', 'Dermatologist'), ('cardiologist', 'Cardiologist'), ('urologist', 'Urologist'), ('dentist', 'Dentist'), ('generalist', 'Generalist'), ('psychiatrist', 'Psychiatrist'), ('radiologist', 'Radiologist')], default='generalist', max_length=40)),
                ('description', models.TextField()),
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('services', models.ManyToManyField(default=None, related_name='doctor_services', to='doctorBackOffice.Service')),
            ],
        ),
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='bill', to='doctorBackOffice.appointment')),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='services',
            field=models.ManyToManyField(default=None, related_name='appointment_services', to='doctorBackOffice.Service'),
        ),
    ]
