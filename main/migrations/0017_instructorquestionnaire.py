# Generated by Django 4.2.5 on 2023-11-09 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_student_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstructorQuestionnaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('question', models.CharField(max_length=500)),
            ],
        ),
    ]