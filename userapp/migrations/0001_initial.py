# Generated by Django 5.0.7 on 2024-10-01 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('date', models.DateField()),
                ('first_name', models.CharField(max_length=20)),
                ('symptoms', models.CharField(max_length=200)),
            ],
        ),
    ]