# Generated by Django 5.0.3 on 2024-04-09 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0002_user_profile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user_profile',
            new_name='UserProfile',
        ),
    ]
