from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(
        r'mark_word_viewed/(?P<word_id>\d+)/$',
        'words.views.mark_word_viewed',
        name='mark_word_viewed',
    ),
    url(
        r'mark_group_viewed/(?P<word_group_id>\d+)/$',
        'words.views.mark_group_viewed',
        name='mark_group_viewed',
    ),
)