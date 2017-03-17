from django.conf.urls import url, include

from slate2learn import views

urlpatterns = [
    url(r'^profile/(?P<pk>[0-9]+)/$', view=views.profile, name="profile"),
    url(r'^repopulate/$', views.repopulate_db, name="repopulate"),
    url(r'^centre/(?P<pk>[0-9]+)/$', views.centre_view, name="centre"),
    url(r'^centre/learners/$', views.centre_learners, name="centre_learners"),
    url(r'^centre/(?P<pk>[0-9]+)/join_rate/$', views.centre_join_rate, name='centre_join_rate'),
    url(r'^$', views.home, name="home")
]
