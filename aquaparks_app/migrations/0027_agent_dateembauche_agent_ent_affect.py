# Generated by Django 4.1.3 on 2023-08-30 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aquaparks_app', '0026_alter_agent_sexe_alter_conjointe_sexe_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='dateembauche',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='agent',
            name='ent_affect',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]