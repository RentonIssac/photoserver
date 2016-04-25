"""photoserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

import photoserver.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test_show_xml$', photoserver.views.test_show_xml),
    url(r'^upload/$', photoserver.views.upload, name='upload'),
    url(r'^upload_json/$', photoserver.views.upload_json, name='upload_json'),
    url(r'^upload_json_check_exist/$', photoserver.views.upload_json_check_exist, name='upload_json_check_exist'),
    #url(r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root': photoserver.settings.STATICFILES_DIRS, 'show_indexes': True}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
