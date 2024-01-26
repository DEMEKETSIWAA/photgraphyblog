from django.urls import path
from minimistapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('course/', views.course, name='course'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
]