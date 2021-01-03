import os
import json

from django.core.management.base import BaseCommand

from annonces import db
from annonces.models import Symposium

DATA_DIR = os.path.join('annonces', 'data')

class Command(BaseCommand):

    def handle(self, *args, **options):
        fnames = [f for f in os.listdir(DATA_DIR) if f.endswith('.json')]
        fnames.remove('template.json')
        Symposium.objects.all().delete()
        for fname in fnames:
            self.stdout.write(fname)
            with open(os.path.join(DATA_DIR, fname)) as f:
                data = json.load(f)
                db.post(data)
