# Generated by Django 5.0.3 on 2024-04-19 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0010_jobapplication'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapplication',
            name='resume',
            field=models.FileField(upload_to='applicant_resumes/'),
        ),
    ]
