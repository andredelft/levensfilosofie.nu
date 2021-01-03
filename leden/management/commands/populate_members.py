import os
import json

from django.core.management.base import BaseCommand

from leden.models import Member

SOURCE_FILENAME = os.path.join('data', 'leden', 'leden.json')

class Command(BaseCommand):

    def handle(self, *args, **options):
        Member.objects.all().delete()
        with open(SOURCE_FILENAME) as f:
            data = json.load(f)
            Member.objects.bulk_create(Member(**member_data) for member_data in data)
