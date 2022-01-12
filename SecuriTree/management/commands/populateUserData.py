import json
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from SecuriTree.models import User

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str)

    def handle(self, *args, **options):
        with open(options['json_file']) as f:
            data_list = json.load(f)

        for data in data_list['registered_users']:
            data['pk'] = data.pop('username')
            data['password'] = make_password(data.pop('password'))
            User.objects.get_or_create(pk=data['pk'], defaults=data)
