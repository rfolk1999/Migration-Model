# Generated by Django 3.2.1 on 2021-05-12 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dapp', '0003_rental'),
    ]

    operations = [
        migrations.CreateModel(
            name='CorMatrix',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_in_id', models.IntegerField()),
                ('district_out_id', models.IntegerField()),
                ('count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Districts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_id', models.IntegerField()),
                ('district_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Rental',
        ),
    ]