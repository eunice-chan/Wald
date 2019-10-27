from django.shortcuts import render

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'homepage/detail.html'
