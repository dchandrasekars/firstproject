# Generated by Django 5.1.2 on 2024-10-29 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_phone'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Member',
            new_name='NewMembers',
        ),
    ]
