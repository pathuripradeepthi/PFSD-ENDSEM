# Generated by Django 5.0.6 on 2024-12-07 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_appointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rescheduling',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('PrevSchedule_Time', models.DateTimeField()),
                ('NewSchedule_time', models.DateTimeField(blank=True, null=True)),
                ('Doctor_dep', models.CharField(max_length=30)),
            ],
        ),
    ]
