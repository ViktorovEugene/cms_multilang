from django.contrib import admin

from zinnia.models.entry import Entry
from zinnia_ckeditor.admin import EntryAdminCKEditor

from .models import CountryFlag


class EntryGalleryAdmin(EntryAdminCKEditor):
    fieldsets = (
        ('Content', {
          'fields': (('title', 'status'), 'lead', 'content',)}),
        ('Location visibility', {
          'fields': ('country_flag',),
          'classes': ('collapse', 'collapse-closed')}),) + \
        EntryAdminCKEditor.fieldsets[2:]


class CountryFlagAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation')

admin.site.register(Entry, EntryGalleryAdmin)
admin.site.register(CountryFlag, CountryFlagAdmin)