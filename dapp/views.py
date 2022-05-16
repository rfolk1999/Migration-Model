from django.shortcuts import render
from django.http import JsonResponse

from django.shortcuts import render
from django.db import models
from django_google_maps import fields as map_fields

from .models import PassengerTurnover, Districts, CorMatrix

from django.http import HttpResponse
import mimetypes
import os

def show_turnover(request):
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, 'dapp/show_turnover.html', {'mapbox_access_token': mapbox_access_token})  

def show_matrices(request):
    data = CorMatrix.objects
    fp = open('C:\games\matrices.xls', "rb");
    response = HttpResponse(fp.read());
    fp.close();
    file_type = mimetypes.guess_type('C:\games\matrices.xls');
    if file_type is None:
        file_type = 'application/octet-stream';
    response['Content-Type'] = file_type
    response['Content-Length'] = str(os.stat('C:\games\matrices.xls').st_size);
    response['Content-Disposition'] = "attachment; filename=correspondense.xls";
    return response;
    #return render(request, 'dapp/show_matrices.html', {'data': data})  

def show_charts(request):
    return render(request, 'dapp/show_charts.html', {})  

def show_tables(request):
    """ data = CorMatrix.objects
    fp = open('C:\games\characteristics.xls', "rb");
    response = HttpResponse(fp.read());
    fp.close();
    file_type = mimetypes.guess_type('C:\games\characteristics.xls');
    if file_type is None:
        file_type = 'application/octet-stream';
    response['Content-Type'] = file_type
    response['Content-Length'] = str(os.stat('C:\games\characteristics.xls').st_size);
    response['Content-Disposition'] = "attachment; filename=characteristics.xls";
    return response; """
    return render(request, 'dapp/show_charts.html', {})  
    
def show_character(request):
    data = CorMatrix.objects
    fp = open('C:\games\matrices.xls', "rb");
    response = HttpResponse(fp.read());
    fp.close();
    file_type = mimetypes.guess_type('C:\games\matrices.xls');
    if file_type is None:
        file_type = 'application/octet-stream';
    response['Content-Type'] = file_type
    response['Content-Length'] = str(os.stat('C:\games\matrices.xls').st_size);
    response['Content-Disposition'] = "attachment; filename=correspondense.xls";
    return response;
    """ data = CorMatrix.objects
    fp = open('C:\games\characteristics.xls', "rb");
    response = HttpResponse(fp.read());
    fp.close();
    file_type = mimetypes.guess_type('C:\games\characteristics.xls');
    if file_type is None:
        file_type = 'application/octet-stream';
    response['Content-Type'] = file_type
    response['Content-Length'] = str(os.stat('C:\games\characteristics.xls').st_size);
    response['Content-Disposition'] = "attachment; filename=characteristics.xls";
    return response; """

def show_criterion(request):
    return render(request, 'dapp/show_tables.html', {}) 
    