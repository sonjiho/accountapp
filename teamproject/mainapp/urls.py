from django.urls import path
from .views import *

app_name='mainapp'

urlpatterns = [
    path('', mainpage, name='mainpage'),
]