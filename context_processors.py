from django.contrib.sites.models import Site
from django.contrib.contenttypes.models import ContentType
from django.conf import settings


def current_site(request):
    return {'current_site': Site.objects.get_current()}
