from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^$', 'how_to_teach_your_baby_to_tracker.views.dash', name='dash'),
    url(
        r'^manage/$',
        'how_to_teach_your_baby_to_tracker.views.manage',
        name='manage',
    ),
    url(r'^words/', include('words.urls', namespace='words')),
    url(r'^admin/', include(admin.site.urls)),
)
