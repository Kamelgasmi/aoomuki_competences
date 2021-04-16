# Generated by Django 3.1.5 on 2021-02-15 13:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0056_auto_20210215_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='profil',
            name='certification',
            field=models.ManyToManyField(blank=True, related_name='collaboraters', to='app.ListCertification'),
        ),
        migrations.RemoveField(
            model_name='listcertification',
            name='user',
        ),
        migrations.AddField(
            model_name='listcertification',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur '),
        ),
    ]