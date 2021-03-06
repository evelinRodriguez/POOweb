# Generated by Django 2.1.5 on 2019-01-08 01:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cuencas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombrecuenca', models.CharField(max_length=250)),
                ('contaminacion', models.CharField(max_length=500)),
                ('combatir_contaminacion', models.CharField(max_length=100)),
                ('direccionp', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='partes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('periodico', models.CharField(max_length=100)),
                ('tituloN', models.CharField(max_length=1000)),
                ('cuencas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.cuencas')),
            ],
        ),
    ]
