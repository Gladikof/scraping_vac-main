from unicodedata import name
from django.shortcuts import render
import datetime



def home(request):
    
    date = datetime.datetime.now().date()
    name ='Dati'
    mycontext = {'date':date , 'name' : name}
    return render(request, 'home.html', mycontext) 