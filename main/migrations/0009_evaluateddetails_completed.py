# Generated by Django 4.2.5 on 2023-09-28 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_subinstsec_evaluateddetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluateddetails',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]