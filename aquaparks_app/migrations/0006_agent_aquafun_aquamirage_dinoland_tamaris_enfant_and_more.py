# Generated by Django 4.1.3 on 2023-08-20 13:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aquaparks_app', '0005_alter_customuser_email_alter_customuser_first_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matricule', models.CharField(max_length=20, unique=True)),
                ('cin', models.CharField(blank=True, max_length=20)),
                ('categorie', models.CharField(choices=[('hc', 'HC'), ('tam', 'TAM'), ('oe', 'OE')], max_length=5)),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=50)),
                ('datenaissance', models.DateField(blank=True, verbose_name='date de naissance')),
                ('sexe', models.CharField(choices=[('m', 'Masculin'), ('f', 'Feminin')], max_length=2)),
                ('adulte_enfant', models.CharField(choices=[('adulte', 'Adulte'), ('enfant', 'Enfant')], default='adulte', max_length=10)),
                ('accord', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='AquaFun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prix_adulte_dejeuner', models.IntegerField(default=50)),
                ('prix_enfant_dejeuner', models.IntegerField(default=40)),
                ('prix_adulte', models.IntegerField(default=40)),
                ('prix_enfane', models.IntegerField(default=30)),
                ('no_reserve', models.IntegerField(default=0)),
                ('no_reservation_reste', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AquaMirage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prix_adulte_dejeuner', models.IntegerField(default=50)),
                ('prix_enfant_dejeuner', models.IntegerField(default=40)),
                ('prix_adulte', models.IntegerField(default=40)),
                ('prix_enfane', models.IntegerField(default=30)),
                ('no_reserve', models.IntegerField(default=0)),
                ('no_reservation_reste', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DinoLand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prix_adulte', models.IntegerField(default=30)),
                ('prix_enfant', models.IntegerField(default=25)),
                ('no_reserve', models.IntegerField(default=0)),
                ('no_reservation_reste', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tamaris',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prix_adulte', models.IntegerField(default=40)),
                ('prix_enfant', models.IntegerField(default=30)),
                ('no_reserve', models.IntegerField(default=0)),
                ('no_reservation_reste', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Enfant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.DecimalField(decimal_places=2, max_digits=4)),
                ('cin', models.CharField(blank=True, max_length=20)),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=50)),
                ('datenaissance', models.DateField(verbose_name='date de naissance')),
                ('sexe', models.CharField(choices=[('m', 'Masculin'), ('f', 'Feminin')], default='f', max_length=2)),
                ('adulte_enfant', models.CharField(choices=[('adulte', 'Adulte'), ('enfant', 'Enfant')], default='adulte', max_length=10)),
                ('accord', models.CharField(max_length=3)),
                ('droit_a_beneficier', models.CharField(choices=[('oui', 'OUI'), ('non', 'NON')], max_length=3)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aquaparks_app.agent')),
            ],
        ),
        migrations.CreateModel(
            name='Conjointe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.DecimalField(decimal_places=2, max_digits=4)),
                ('cin', models.CharField(blank=True, max_length=20)),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=50)),
                ('datenaissance', models.DateField(verbose_name='date de naissance')),
                ('sexe', models.CharField(choices=[('m', 'Masculin'), ('f', 'Feminin')], default='f', max_length=2)),
                ('adulte_enfant', models.CharField(choices=[('adulte', 'Adulte'), ('enfant', 'Enfant')], default='adulte', max_length=10)),
                ('accord', models.CharField(max_length=3)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aquaparks_app.agent')),
            ],
        ),
    ]
