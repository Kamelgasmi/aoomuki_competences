# Generated by Django 3.1.5 on 2021-02-15 12:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0055_auto_20210215_1345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listcertification',
            name='user',
        ),
        migrations.AddField(
            model_name='listcertification',
            name='user',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur '),
        ),
    ]
