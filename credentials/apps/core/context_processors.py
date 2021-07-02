""" Core context processors. """
from django.conf import settings

def core(request):
    """ Site-wide context processor. """
    site = request.site

    return {
        'site': site,
        'language_code': request.LANGUAGE_CODE,
        'platform_name': site.siteconfiguration.platform_name,
        'enhenced_theme': settings.ENHENCED_THEME,
    }
