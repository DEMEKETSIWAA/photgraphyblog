
from django.urls import path
from django.urls import include
from minimistapp import urls as app_urls
urlpatterns = [
    path('',include(app_urls))
]
# this is comment