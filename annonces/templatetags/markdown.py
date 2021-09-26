from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import SafeString
from django.conf import settings

import re
from markdown import markdown

register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def render_markdown(content):
    return SafeString(markdown(content, extensions=['mdx_linkify', 'smarty']))


@register.filter(is_safe=True)
@stringfilter
def render_markdown_line(content):
    if '\n\n' in content:
        if settings.DEBUG:
            raise ValueError('render_markdown_line expects one block (e.g., no double newlines)')
        else:
            content = content.split('\n\n')[0]
    md = render_markdown(content)
    md = re.sub(r'^\s*<p>\s*|\s*</p>\s*$', '', md)
    return SafeString(md)
