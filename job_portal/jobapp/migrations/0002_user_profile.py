# Generated by Django 5.0.3 on 2024-04-09 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
                ('email', models.EmailField(max_length=254)),
                ('birthdate', models.DateField()),
                ('bio', models.TextField(blank=True, null=True)),
                ('phone_number', models.CharField(max_length=15)),
                ('ssc_percentage', models.FloatField()),
                ('hsc_percentage', models.FloatField()),
                ('degree', models.CharField(max_length=100)),
                ('institution', models.CharField(max_length=100)),
                ('graduation_year', models.IntegerField(blank=True, null=True)),
                ('skills', models.TextField()),
                ('resume', models.FileField(blank=True, upload_to='resumes/')),
            ],
        ),
    ]
