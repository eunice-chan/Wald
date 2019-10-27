from django.shortcuts import render
from django.views import generic
from .models import Account

# Create your views here.
def index(request):
    account = Account()
    context =  {
    "user": account
    }
    return render(request, 'homepage/home.html', context)
