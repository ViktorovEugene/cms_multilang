"""Urls for the Zinnia sitemap"""
from django.conf.urls import url

from zinnia_customized.views.sitemap import Sitemap


urlpatterns = [
    url(r'^$', Sitemap.as_view(),
        name='sitemap'),
]
