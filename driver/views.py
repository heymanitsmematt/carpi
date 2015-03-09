from django.shortcuts import render
from django.views.generic import TemplateView

class Drive(TemplateView):
    template_name = 'driver/drive.html'
