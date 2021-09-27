from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin

from .models import Member


@admin.register(Member)
class SymposiumAdmin(SummernoteModelAdmin):
    readonly_fields = ('picture_preview',)
    fields = (
        ('picture_preview', 'picture'),
        'prefix',
        'first_name',
        ('preposition', 'last_name'),
        'suffix',
        'personalia',
    )

    summernote_fields = ['personalia']
