# Generated by Django 4.2.5 on 2023-09-28 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_remove_comment_completed_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Status',
        ),
    ]