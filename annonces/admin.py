from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin, SummernoteInlineModelAdmin

from .models import Symposium, Talk, ProgramItem


class TalkAdmin(SummernoteInlineModelAdmin, admin.StackedInline):
    model = Talk
    fields = (
        'speaker',
        'title',
        'abstract',
        'personalia',
        'video_id'
    )


class ProgramItemAdmin(admin.TabularInline):
    model = ProgramItem
    fields = (
        'time_from',
        'time_to',
        'name'
    )


@admin.register(Symposium)
class SymposiumAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
    fields = (
        'title',
        'introduction',
        'date',
        ('time_from', 'time_to'),
        'place'
    )
    inlines = [ProgramItemAdmin, TalkAdmin]
