from django.db import models
from django.utils.html import mark_safe

from markdownify import markdownify
from lxml.html.clean import Cleaner
from lxml.html.defs import safe_attrs as default_safe_attrs
from markdown import Markdown
import re

REMOVE_ATTRS = {"class"}
SAFE_ATTRS = set(default_safe_attrs) - REMOVE_ATTRS

HTML_CLEANER = Cleaner(
    style=True,
    remove_tags={"span", "br"},
    safe_attrs=SAFE_ATTRS
)

MD_CONVERTER = Markdown(
    extensions=['mdx_linkify', 'smarty', 'tables']
)


class CleanHTMLField(models.TextField):

    def _clean(self, value):
        value = HTML_CLEANER.clean_html(value)
        value = markdownify(value)
        return value

    def pre_save(self, model_instance, add):
        value = super().pre_save(model_instance, add)
        return self._clean(value)

    def from_db_value(self, value, *args, **kwargs):
        return mark_safe(
            MD_CONVERTER.convert(value)
        )


class CleanHTMLLineField(CleanHTMLField):

    def _clean(self, value):
        value = super()._clean(value)
        value = re.sub(r'\s+', ' ', value)
        return value

    def from_db_value(self, value, *args, **kwargs):
        value = super().from_db_value(value, *args, **kwargs)
        value = re.sub(r'^\s*<p>\s*|\s*</p>\s*$', '', value)
        return mark_safe(value)
