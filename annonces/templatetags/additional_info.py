from django import template
from django.template.defaultfilters import stringfilter

from annonces.models import AdditionalInfo
from annonces.templatetags.markdown import render_markdown

register = template.Library()

@register.simple_tag
@stringfilter
def render_info(name):
    try:
        obj = AdditionalInfo.objects.get(name=name)
    except AdditionalInfo.DoesNotExist:
        return ''
    else:
        return render_markdown(obj.content)
