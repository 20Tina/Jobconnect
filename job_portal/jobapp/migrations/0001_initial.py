# Generated by Django 5.0.3 on 2024-03-29 17:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='jobListing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('job_type', models.CharField(choices=[('Full-time', 'Full-time'), ('Part-time', 'Part-time'), ('Contract', 'Contract'), ('Internship', 'Internship')], max_length=20)),
                ('salary', models.CharField(blank=True, max_length=30)),
                ('company_name', models.CharField(max_length=300)),
                ('company_description', models.TextField(blank=True, null=True)),
                ('requirements', models.TextField()),
                ('url', models.URLField()),
                ('last_date', models.DateField()),
                ('is_published', models.BooleanField(default=False)),
                ('is_closed', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('special_instructions', models.TextField(blank=True, null=True)),
                ('logo_image', models.ImageField(upload_to='logos')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Category', to='jobapp.category')),
            ],
        ),
    ]
