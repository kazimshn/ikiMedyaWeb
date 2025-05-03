from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hizmetler/', views.services, name='services'),
    path('hakkimizda/', views.about, name='about'),
    path('iletisim/', views.contact, name='contact'),
] 