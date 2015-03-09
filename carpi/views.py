from django.views.generic import TemplateView, View
from django.http import HttpResponse

class Home(TemplateView):
    template_name = 'carpi/home.html'
	
