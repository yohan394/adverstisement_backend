# Generated by Django 3.1 on 2020-11-19 07:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20201117_1553'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agegroup',
            old_name='age_group',
            new_name='age',
        ),
    ]