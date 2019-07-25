from django.urls import path
from .views import home

app_name = "iBot"

urlpatterns = [
    path('', home,name='home'),
]