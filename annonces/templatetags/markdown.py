from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import SafeString

import re
from markdown import markdown
from mdx_urlize import UrlizeExtension

register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def render_markdown(content):
    return SafeString(markdown(content, extensions=[UrlizeExtension()]))

@register.filter(is_safe=True)
@stringfilter
def render_markdown_line(content):
    if '\n\n' in content:
        raise ValueError('render_markdown_line expects one block (e.g., no double newlines)')
    md = render_markdown(content)
    md = re.sub('^\s*<p>\s*|\s*</p>\s*$', '', md)
    return SafeString(md)
