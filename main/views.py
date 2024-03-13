from django.shortcuts import render
from django.views.generic import TemplateView

""" def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def contact(request):
    return render(request, 'main/contact.html') """

class IndexView(TemplateView):
    template_name = 'main/index.html'

class AboutView(TemplateView):
    template_name = 'main/about.html'

class ContactView(TemplateView):
    template_name = 'main/contact.html'