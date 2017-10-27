from django.core.management.base import BaseCommand

import logging

from django.contrib.auth.models import Group


class Command(BaseCommand):
    help = 'Creates application-wide permissions and groups'
    logger = logging.getLogger('console')

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)

        # These models should have update_relationships
        self.groups = [
            "bureau_ao"
        ]

    def handle(self, *args, **options):
        for group_name in self.groups:
            group = Group.objects.get_or_create(name=group_name)
            if group[1]:
                self.logger.info(f"Created group {group_name}")