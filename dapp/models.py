from django.conf import settings
from django.db import models
from django.utils import timezone

from django.db import models
from django_google_maps import fields as map_fields

class PassengerTurnover(models.Model):
    point_name = models.CharField(max_length=50)
    point_length = models.FloatField()
    point_out = models.IntegerField()
    point_in = models.IntegerField()
    point_filling = models.IntegerField()
    point_turnover = models.FloatField()

class CorMatrix(models.Model):
    district_in_id = models.IntegerField()
    district_out_id = models.IntegerField()
    count = models.IntegerField()

class Districts(models.Model):
    district_id = models.IntegerField()
    district_name = models.CharField(max_length=50)

