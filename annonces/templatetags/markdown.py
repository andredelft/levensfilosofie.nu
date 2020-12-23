from markdown import markdown
from django import template

register = template.Library()

@register.filter
def render_markdown(content):
    return markdown(content)
