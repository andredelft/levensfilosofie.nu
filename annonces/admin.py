from django.contrib import admin

from .models import Symposium, Talk, ProgramItem


class TalkAdmin(admin.StackedInline):
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
class SymposiumAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'introduction',
        'date',
        ('time_from', 'time_to'),
        'place'
    )
    inlines = [ProgramItemAdmin, TalkAdmin]
