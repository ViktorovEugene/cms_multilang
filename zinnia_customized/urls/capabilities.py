"""Urls for the zinnia capabilities"""
from django.conf.urls import url

from zinnia_customized.views.capabilities import RsdXml
from zinnia_customized.views.capabilities import HumansTxt
from zinnia_customized.views.capabilities import OpenSearchXml
from zinnia_customized.views.capabilities import WLWManifestXml


urlpatterns = [
    url(r'^rsd.xml$', RsdXml.as_view(),
        name='rsd'),
    url(r'^humans.txt$', HumansTxt.as_view(),
        name='humans'),
    url(r'^opensearch.xml$', OpenSearchXml.as_view(),
        name='opensearch'),
    url(r'^wlwmanifest.xml$', WLWManifestXml.as_view(),
        name='wlwmanifest'),
]
