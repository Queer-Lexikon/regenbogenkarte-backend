# Generated by Django 4.1.9 on 2023-06-22 08:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organisation',
            old_name='identites',
            new_name='identities',
        ),
    ]