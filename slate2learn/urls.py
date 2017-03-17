from django.conf.urls import url, include

from slate2learn import views

urlpatterns = [
    url(r'^profile/(?P<pk>[0-9]+)/$', view=views.profile, name="profile"),
    url(r'^repopulate/$', views.repopulate_db, name="repopulate")
]
