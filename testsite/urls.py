from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^polls/$', 'testsite.polls.views.index'),
    (r'^polls/(?P<poll_id>\d+)/$', 'testsite.polls.views.detail'),
    (r'^polls/(?P<poll_id>\d+)/results/$', 'testsite.polls.views.results'),
    (r'^polls/(?P<poll_id>\d+)/vote/$', 'testsite.polls.views.vote'),
    (r'^admin/', include(admin.site.urls)),
)

