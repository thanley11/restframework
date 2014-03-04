from django.conf.urls import patterns, url, include
from snippets import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)


#Adds suffixes by adding format arg to snippet functions and appending this to url
#format_suffix_patterns

urlpatterns = patterns('',
        url(r'^', include(router.urls)),
        url(r'^api-auth/', include('rest_framework.urls',
                                   namespace='rest_framework'))
)