from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^profile/(?P<pk>[0-9]+)/$', view=profile, name="profile"),
]
