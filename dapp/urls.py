from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_turnover, name='show_turnover'),
    path('/charts', views.show_charts, name='show_charts'),
    path('/matrices', views.show_matrices, name='show_matrices'),
    path('/tables', views.show_tables, name='show_tables'),
    path('/characteristics', views.show_character, name='show_character'),
    path('/criterion', views.show_tables, name='show_criterion'),

]