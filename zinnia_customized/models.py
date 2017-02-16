from django.conf import settings
from django.db import models
from zinnia.models_bases.entry import AbstractEntry


class CountryFlag(models.Model):
    CMS_LANGUAGES = [
        ('', '---'),
    ]
    CMS_LANGUAGES.extend((lc, lc) for lc in next(zip(*settings.LANGUAGES)))

    name = models.CharField(max_length=128)
    abbreviation = models.CharField(max_length=4)
    lang_code = models.CharField(
        max_length=20, blank=True,
        choices=CMS_LANGUAGES,
        default=CMS_LANGUAGES[0][0]
    )

    def __str__(self):
        return self.name


class EntryLocation(AbstractEntry):
    country_flag = models.ManyToManyField(
        CountryFlag, related_name='blog_entry_country_flag', blank=True
    )

    def __str__(self):
        return 'Entry %s' % self.title

    class Meta(AbstractEntry.Meta):
        abstract = True