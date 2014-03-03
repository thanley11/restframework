from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = patterns('snippets.views',
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    )
    
#Adds suffixes by adding format arg to snippet functions and appending this to url
urlpatterns = format_suffix_patterns(urlpatterns)    