# Generated by Django 3.1.5 on 2021-03-08 08:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0075_auto_20210308_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofil',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur '),
        ),
    ]