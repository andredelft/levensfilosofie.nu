from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin, SummernoteInlineModelAdmin
from django_summernote.widgets import SummernoteWidget

from .models import Symposium, Talk, ProgramItem
from .fields import CleanHTMLLineField

TOOLBAR_CONFIG = [
    ['style', ['bold', 'italic', 'clear']],
    ['font', ['strikethrough', 'superscript', 'subscript']]
]

CLEAN_HTML_LINE_TABULAR_OVERRIDE = {
    CleanHTMLLineField: {'widget': SummernoteWidget(
        attrs={
            'summernote': {
                'width': '100%',
                'height': '150px',
                'toolbar': TOOLBAR_CONFIG
            }
        }
    )}
}

CLEAN_HTML_LINE_OVERRIDE = {
    CleanHTMLLineField: {'widget': SummernoteWidget(
        attrs={
            'summernote': {
                'height': '100px',
                'toolbar': TOOLBAR_CONFIG
            }
        }
    )}
}


class TalkAdmin(SummernoteInlineModelAdmin, admin.StackedInline):
    model = Talk
    fields = (
        'speaker',
        'title',
        'abstract',
        'personalia',
        'video_id'
    )

    summernote_fields = [
        'abstract', 'personalia'
    ]
    formfield_overrides = CLEAN_HTML_LINE_OVERRIDE

    # class Meta:
    #     help_texts = {
    #         'video_id':
    #     }


class ProgramItemAdmin(SummernoteInlineModelAdmin, admin.TabularInline):
    model = ProgramItem
    fields = (
        'time_from',
        'time_to',
        'name'
    )

    summernote_fields = []
    formfield_overrides = CLEAN_HTML_LINE_TABULAR_OVERRIDE


@admin.register(Symposium)
class SymposiumAdmin(SummernoteModelAdmin):
    fields = (
        'title',
        'introduction',
        'date',
        ('time_from', 'time_to'),
        'place'
    )
    inlines = [ProgramItemAdmin, TalkAdmin]

    summernote_fields = ['introduction']
    formfield_overrides = CLEAN_HTML_LINE_OVERRIDE
