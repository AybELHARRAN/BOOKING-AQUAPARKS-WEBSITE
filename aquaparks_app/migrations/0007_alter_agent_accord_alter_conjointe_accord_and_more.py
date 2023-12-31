# Generated by Django 4.1.3 on 2023-08-20 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aquaparks_app', '0006_agent_aquafun_aquamirage_dinoland_tamaris_enfant_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='accord',
            field=models.CharField(choices=[('oui', 'OUI'), ('non', 'NON')], max_length=3),
        ),
        migrations.AlterField(
            model_name='conjointe',
            name='accord',
            field=models.CharField(choices=[('oui', 'OUI'), ('non', 'NON')], max_length=3),
        ),
        migrations.AlterField(
            model_name='enfant',
            name='accord',
            field=models.CharField(choices=[('oui', 'OUI'), ('non', 'NON')], max_length=3),
        ),
    ]
