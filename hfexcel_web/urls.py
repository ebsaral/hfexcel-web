from django.conf.urls import url
from django.contrib import admin

import web.views as web_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', web_views.DocumentManagerView.as_view(), name='web')
]
