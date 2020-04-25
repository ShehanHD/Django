from django.contrib import admin
from .models import services,gallery,about,team,event
# Register your models here.

admin.site.register(event)
admin.site.register(services)
admin.site.register(gallery)
admin.site.register(about)
admin.site.register(team)