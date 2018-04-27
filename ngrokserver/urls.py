from django.conf.urls import include, url
from django.contrib import admin
from ngrokapp.views import *

urlpatterns = [
    # Examples:
    # url(r'^$', 'ngrokserver.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', request_ngrok)
]
