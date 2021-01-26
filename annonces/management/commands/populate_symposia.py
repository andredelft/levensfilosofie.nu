import os
import json

from django.core.management.base import BaseCommand

from annonces import db
from annonces.models import Symposium, AdditionalInfo

DATA_DIR = os.path.join('data', 'annonces')

class Command(BaseCommand):

    def handle(self, *args, **options):
        dir_inv = os.listdir(DATA_DIR)

        fnames = [f for f in dir_inv if f.endswith('.json')]
        fnames.remove('template.json')
        Symposium.objects.all().delete()
        for fname in fnames:
            with open(os.path.join(DATA_DIR, fname)) as f:
                data = json.load(f)
                db.post_symposium(data)

        fnames = [f for f in dir_inv if f.endswith('.md')]
        AdditionalInfo.objects.all().delete()
        for fname in fnames:
            with open(os.path.join(DATA_DIR, fname)) as f:
                obj = AdditionalInfo(name=os.path.splitext(fname)[0], content=f.read())
                obj.save()
