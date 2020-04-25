from django.shortcuts import render
from .models import quotes
# Create your views here.

def quotes_page(request):
    return render(request, 'quotes.temp.html', {'quotes':quotes.objects.all()} )