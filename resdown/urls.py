

from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from myapp.api import ResList, Base, DownRes


urlpatterns = [
    path('',Base.as_view(),name='Base'),
    path('admin/', admin.site.urls),
    url(r'^api/res_list/$',ResList.as_view(),name='res_list'),
    url(r'^api/res_list/(?P<unique_identifier>[0-9a-f\-]+)/$',DownRes.as_view(),name='down_res'),
]
