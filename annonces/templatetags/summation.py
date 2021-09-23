from django import template

register = template.Library()


@register.filter
def dutch_summation(values_list):
    string_list = [str(item) for item in values_list]
    if len(string_list) == 1:
        return values_list[0]
    else:
        return f"{', '.join(string_list[:-1])} en {string_list[-1]}"
