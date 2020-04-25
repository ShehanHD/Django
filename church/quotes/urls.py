from django.urls import path, include

from . import views

urlpatterns = [
    path('quotes_page', views.quotes_page)
]
