from django.urls import path
from django.conf.urls import url
from .views import RegistrationAPIView, FetchUpdateDeleteDatails, LoginAPIView


#app_name = 'authentication'
urlpatterns = [

    path('users/', RegistrationAPIView.as_view()),
    url(r'^user/(?P<pk>[a-z]+)$', FetchUpdateDeleteDatails.as_view()),
    url(r'^users/login/?$', LoginAPIView.as_view()),
]
