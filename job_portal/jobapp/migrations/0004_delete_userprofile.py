# Generated by Django 5.0.3 on 2024-04-09 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0003_rename_user_profile_userprofile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
