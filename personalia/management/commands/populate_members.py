import os
import json

from django.core.management.base import BaseCommand

from personalia.models import Member

SOURCE_FILENAME = os.path.join('personalia', 'data', 'personalia.json')

class Command(BaseCommand):

    def handle(self, *args, **options):
        with open(SOURCE_FILENAME) as f:
            data = json.load(f)
            Member.objects.bulk_create(Member(**member_data) for member_data in data)
