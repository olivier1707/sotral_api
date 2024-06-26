# Generated by Django 5.0.3 on 2024-04-25 09:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idbus', models.IntegerField()),
                ('nomconducteur', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tarif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idtarif', models.IntegerField()),
                ('codeTarif', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idUser', models.IntegerField()),
                ('codeUser', models.CharField(max_length=50)),
                ('telephone', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ligne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idligne', models.IntegerField()),
                ('codeLigne', models.CharField(max_length=50)),
                ('libelleLigne', models.CharField(max_length=50)),
                ('Bus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ligne', to='api_appli.bus')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idsection', models.IntegerField()),
                ('codeSection', models.CharField(max_length=50)),
                ('libelleSection', models.CharField(max_length=50)),
                ('Ligne', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='section', to='api_appli.ligne')),
            ],
        ),
        migrations.CreateModel(
            name='Voyager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idvoyage', models.IntegerField()),
                ('codeVoyage', models.CharField(max_length=50)),
                ('Utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='voyage', to='api_appli.utilisateur')),
            ],
        ),
    ]
