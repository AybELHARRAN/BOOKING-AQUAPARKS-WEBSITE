# Generated by Django 4.1.3 on 2023-08-29 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aquaparks_app', '0022_alter_agent_aquafun_reservations_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enfant',
            name='aquafun_reservations',
            field=models.CharField(default='0', max_length=2),
        ),
        migrations.AlterField(
            model_name='enfant',
            name='aquamirage_reservations',
            field=models.CharField(default='0', max_length=2),
        ),
        migrations.AlterField(
            model_name='enfant',
            name='dinoland_reservations',
            field=models.CharField(default='0', max_length=2),
        ),
        migrations.AlterField(
            model_name='enfant',
            name='tamaris_reservations',
            field=models.CharField(default='0', max_length=2),
        ),
    ]
