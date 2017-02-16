"""Defaults urls for the Zinnia project"""
from django.conf.urls import url
from django.conf.urls import include

from django.utils.translation import ugettext_lazy

from zinnia.settings import TRANSLATED_URLS


def i18n_url(url, translate=TRANSLATED_URLS):
    """
    Translate or not an URL part.
    """
    if translate:
        return ugettext_lazy(url)
    return url

_ = i18n_url

app_name = 'zinnia'

urlpatterns = [
    url(_(r'^feeds/'), include('zinnia_customized.urls.feeds')),
    url(_(r'^tags/'), include('zinnia_customized.urls.tags')),
    url(_(r'^authors/'), include('zinnia_customized.urls.authors')),
    url(_(r'^categories/'), include('zinnia_customized.urls.categories')),
    url(_(r'^search/'), include('zinnia_customized.urls.search')),
    url(_(r'^random/'), include('zinnia_customized.urls.random')),
    url(_(r'^sitemap/'), include('zinnia_customized.urls.sitemap')),
    url(_(r'^trackback/'), include('zinnia_customized.urls.trackback')),
    url(_(r'^comments/'), include('zinnia_customized.urls.comments')),
    url(r'^', include('zinnia_customized.urls.entries')),
    url(r'^', include('zinnia_customized.urls.archives')),
    url(r'^', include('zinnia_customized.urls.shortlink')),
    url(r'^', include('zinnia_customized.urls.quick_entry')),
    url(r'^', include('zinnia_customized.urls.capabilities')),
]
