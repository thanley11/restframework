from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('snippets.views',
    url(r'^snippets/$', 'snippet_list'),
    url(r'^snippets/(?P<pk>[0-9]+)/$', 'snippet_detail'),
    )
    
#Adds suffixes by adding format arg to snippet functions and appending this to url
urlpatterns = format_suffix_patterns(urlpatterns)    