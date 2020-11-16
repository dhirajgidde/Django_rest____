from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/tutorials$', views.tuterial_list),
    url(r'^api/tutorials/(?P<pk>[0-9]+)$', views.tuterial_detail),
    url(r'^api/tutorials/published$', views.tuterial_list_published)
]
