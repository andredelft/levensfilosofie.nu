from django import template
import datetime

register = template.Library()

SOON_DAY_RANGE = 14
NOW = datetime.date.today()


@register.filter
def is_soon(symposium):
    days_until = (symposium.date - NOW).days
    return days_until > 0 and days_until <= SOON_DAY_RANGE
