from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.show_about, name='about'),
    path('contacts/', views.show_contact, name='contacts')
]
