from django.urls import path
from .views import home,emin

urlpatterns = [
    path('',home,name='home'),
    path('def/',emin,name='emin')
]
