# Generated by Django 3.1.7 on 2021-03-30 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_employee_vacation'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacation',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='polls.employee'),
        ),
    ]
