# Generated by Django 3.1.7 on 2021-03-30 21:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0004_auto_20210331_0021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacation',
            name='employee',
        ),
        migrations.AddField(
            model_name='vacation',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
