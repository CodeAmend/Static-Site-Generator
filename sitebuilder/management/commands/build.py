import os
import shutil

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError
from django.core.urlresolvers import reverse
from django.test.client import Client


def get_pages():
    for name in os.listdir(settings.SITE_PAGES_DIRECTORY):
        if name.endswith('.html'):
            yield name[:-5]


class Command(BaseCommand):
    help = 'Build static site output.'
    leave_locale_alone = True

    def handle(self, *args, **options):
        """Request pages and build output."""
