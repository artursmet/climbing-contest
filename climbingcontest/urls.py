from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^$', 'core.views.homepage', name='homepage'),
    url(r'^zapisy/(?P<contest_pk>\d+)/$', 'contest.views.subscribe', name='subscribe'),
    url(r'^lista-zawodnikow/(?P<contest_pk>\d+)/$', 'contest.views.all_groups', name='all_groups'),
    url(r'^lista-zawodnikow/(?P<contest_pk>\d+)/csv/$', 'contest.views.create_csv_list', name='create_csv_list'),

)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
