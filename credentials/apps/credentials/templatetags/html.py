"""
Template tags and helper functions for escaping script tag.
"""
import json
from django import template
from django.template.defaultfilters import date
from django.utils.translation import get_language
from django.utils.safestring import mark_safe
register = template.Library()


@register.filter(expects_localtime=True, is_safe=False)
def month(value):
    """
    Provides the month from a provided date as a string.

    This is used to work around a bug in the Spanish django month translations.
    See LEARNER-3859 for more details.

    Arguments:
        value (datetime): date to format

    Returns:
        string: A formatted version of the month
    """
    formatted = date(value, 'E')

    language = get_language()
    if language and language.split('-')[0].lower() == 'es':
        return formatted.lower()

    return formatted


@register.filter
def escape_json(data):
    """
    Escape a JSON string (or convert a dict to a JSON string, and then
    escape it) for being embedded within an HTML template.
    """
    json_string = json.dumps(data) if isinstance(data, dict) else data
    json_string = json_string.replace("&", "\\u0026")
    json_string = json_string.replace(">", "\\u003e")
    json_string = json_string.replace("<", "\\u003c")
    return mark_safe(json_string)