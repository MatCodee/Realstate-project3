from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeView,name='home'),
    path('about/',views.AboutView,name='about'),
    path('services/',views.ServicesView,name='services'),
    path('contact/',views.ContactView,name='contact'),
    path('team/',views.TeamView,name='team'),
    path('properties/',views.PropertyView,name='properties'),
    path('detail/<int:id>',views.DetailPropertyView,name='detail'),

]
