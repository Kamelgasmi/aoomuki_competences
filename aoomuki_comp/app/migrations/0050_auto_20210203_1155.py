# Generated by Django 3.1.5 on 2021-02-03 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0049_auto_20210203_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listofcompetence',
            name='ListInterest',
            field=models.CharField(choices=[(0, 'Aucun'), (1, 'Des notions'), (2, 'Débutant'), (3, 'Intermédiaire'), (4, 'Confirmé')], default='0', max_length=10, unique=True, verbose_name='valeur'),
        ),
        migrations.AlterField(
            model_name='listofcompetence',
            name='ListLevel',
            field=models.CharField(choices=[(0, 'Aucun'), (1, 'Des notions'), (2, 'Débutant'), (3, 'Intermédiaire'), (4, 'Confirmé')], default='0', max_length=10, unique=True, verbose_name='valeur'),
        ),
    ]