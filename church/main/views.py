from django.shortcuts import render
from .models import event, services, gallery, about, team

# Create your views here.


def home(request):

    data = {
        'services':services.objects.all(),
        'event':event.objects.all(),
        'gallery':gallery.objects.all(),
        'about':about.objects.all(),
        'team':team.objects.all(),
    }

    return render(request, 'index.html',  data)
