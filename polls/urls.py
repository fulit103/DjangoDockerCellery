

from . import views
from django.conf.urls import url

urlpatterns = [
    url('correo', views.index, name='index'),
]