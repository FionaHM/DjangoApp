# snippets/urls.py

from django.conf.urls import url, include
from snippets import views

urlpatterns = [ 
    url(r'^$', views.HomePageView.as_view())
]