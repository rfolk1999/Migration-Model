from django.contrib import admin
from .models import PassengerTurnover, Districts, CorMatrix

import json 
from django.contrib import admin
from django.contrib import admin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

admin.site.register(PassengerTurnover)
admin.site.register(Districts)
admin.site.register(CorMatrix)
