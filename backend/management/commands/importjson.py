from django.core.management.base import BaseCommand, CommandError
from backend.models import Organisation
import argparse
import json


class Command(BaseCommand):
    help = "Imports the specified json file into the database"

    def add_arguments(self, parser):
        parser.add_argument("input_file", nargs=1, type=argparse.FileType('r'))

    def handle(self, *args, **options):
        json_content = json.load(options["input_file"][0])
        for json_org in json_content:
            if 'address' in json_org['location']:
                json_org['address'] = json_org['location']['address']
            if 'approx' in json_org['location']:
                json_org['lat_lon_approx'] = json_org['location']['approx']
            json_org['lat'] = json_org['location']['lat']
            json_org['lon'] = json_org['location']['lon']
            del json_org['location']

            org = Organisation()
            for (k,v) in json_org.items():
                setattr(org,k,v)
            org.save()


