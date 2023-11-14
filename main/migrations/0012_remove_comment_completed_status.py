# Generated by Django 4.2.5 on 2023-09-28 09:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_remove_evaluateddetails_submitted_comment_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='completed',
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_complete', models.BooleanField(default=False)),
                ('eval_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.evaluateddetails')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]