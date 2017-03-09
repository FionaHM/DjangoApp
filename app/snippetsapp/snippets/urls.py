# snippets/urls.py

from django.conf.urls import url, include
from snippets import views

urlpatterns = [ 
    url(r'^delete/(?P<pk>\d+)/item/$', views.delete_item, name='delete_item'),
    url(r'^edit/(?P<pk>\d+)/item/$', views.edit_item, name='edit_item'),
    url(r'^update_item/$', views.update_item, name='update_item'),
    url(r'^add/$', views.HomePageView.as_view()),
    url(r'^$', views.HomePageView.as_view()),
]