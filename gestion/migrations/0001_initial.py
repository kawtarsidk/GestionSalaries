# Generated by Django 3.0.6 on 2020-05-20 02:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BulletinPaie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prime', models.IntegerField()),
                ('p_impot', models.IntegerField()),
                ('p_cnss', models.IntegerField()),
                ('p_cimr', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Compte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('matricule', models.CharField(max_length=20)),
                ('nom', models.CharField(max_length=30)),
                ('prenom', models.CharField(max_length=30)),
                ('cin', models.CharField(max_length=10)),
                ('adresse', models.CharField(max_length=150)),
                ('telephone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=200)),
                ('dateNaissance', models.DateField()),
                ('departement', models.CharField(max_length=30)),
                ('emploiOccupe', models.CharField(max_length=30)),
                ('Anciennete', models.IntegerField()),
                ('salaireBase', models.IntegerField()),
                ('compte', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='gestion.Compte')),
                ('bulletinPaie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion.BulletinPaie')),
            ],
        ),
        migrations.CreateModel(
            name='RH',
            fields=[
                ('employe_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gestion.Employe')),
            ],
            bases=('gestion.employe',),
        ),
        migrations.CreateModel(
            name='Salarie',
            fields=[
                ('employe_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gestion.Employe')),
            ],
            bases=('gestion.employe',),
        ),
    ]
