# Generated by Django 3.2.1 on 2021-05-04 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PassengerTurnover',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point_name', models.CharField(max_length=50)),
                ('point_length', models.IntegerField()),
                ('point_out', models.IntegerField()),
                ('point_in', models.IntegerField()),
                ('point_filling', models.IntegerField()),
                ('point_turnover', models.IntegerField()),
            ],
        ),
    ]
