# Generated by Django 4.2.5 on 2023-09-22 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_subinstsec_inst'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subinstsec',
            name='inst',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.instructor'),
        ),
    ]
