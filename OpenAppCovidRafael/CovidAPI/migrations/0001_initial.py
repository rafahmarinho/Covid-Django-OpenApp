# Generated by Django 4.0.3 on 2022-03-08 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Country', models.CharField(max_length=50)),
                ('Code', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('lastChange', models.DateTimeField(auto_now=True)),
                ('lastUpdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='StatisticsCVD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Confirmed', models.IntegerField()),
                ('Recovered', models.IntegerField()),
                ('Critical', models.IntegerField()),
                ('Deaths', models.IntegerField()),
            ],
        ),
    ]
