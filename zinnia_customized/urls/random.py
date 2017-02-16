"""Urls for Zinnia random entries"""
from django.conf.urls import url

from zinnia_customized.views.random import EntryRandom


urlpatterns = [
    url(r'^$',
        EntryRandom.as_view(),
        name='entry_random'),
]
