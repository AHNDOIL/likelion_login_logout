# Generated by Django 4.0.4 on 2022-05-28 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]