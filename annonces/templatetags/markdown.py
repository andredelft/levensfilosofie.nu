from django import template

from markdown import markdown
from mdx_urlize import UrlizeExtension

register = template.Library()

@register.filter
def render_markdown(content):
    return markdown(content, extensions=[UrlizeExtension()])
