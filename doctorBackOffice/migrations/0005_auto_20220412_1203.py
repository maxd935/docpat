# Generated by Django 3.1.1 on 2022-04-12 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctorBackOffice', '0004_alter_doctorinfo_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='time',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='doctorinfo',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='service',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
