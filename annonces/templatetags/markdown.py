from django import template

import re
from markdown import markdown
from mdx_urlize import UrlizeExtension

register = template.Library()

@register.filter
def render_markdown(content):
    return markdown(content, extensions=[UrlizeExtension()])

@register.filter
def render_markdown_line(content):
    if '\n' in content:
        raise ValueError('render_markdown_line expects one line (e.g., no newlines)')
    md = render_markdown(content)
    return re.sub('^\s*<p>\s*|\s*</p>\s*$', '', md)
