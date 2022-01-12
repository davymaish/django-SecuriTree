import json
from django.core.management.base import BaseCommand
from SecuriTree.models import Door, Area, AccessRule

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str)

    def handle(self, *args, **options):
        with open(options['json_file']) as f:
            data_list = json.load(f)

        for data in data_list['system_data']['areas']:
            data['pk'] = data.pop('id')
            data['parent_area'] = Area.objects.filter(pk = data.pop('parent_area')).first()

            # Remove key because child areas have parent id. Data redundancy avoidance
            # It also gives room for Areas to be nested to any depth (Epiuse System Entity Requirement)
            del data['child_area_ids'] 

            Area.objects.get_or_create(pk=data['pk'], defaults=data)

        for data in data_list['system_data']['doors']:
            data['pk'] = data.pop('id')
            data['parent_area'] = Area.objects.get(pk = data.pop('parent_area'))
            Door.objects.get_or_create(pk=data['pk'], defaults=data)

        for data in data_list['system_data']['access_rules']:
            data['pk'] = data.pop('id')
            doors = data.pop('doors');
            rule = AccessRule.objects.get_or_create(pk=data['pk'], defaults=data)

            for door_id in doors:
                Door.objects.get(id=door_id).accessrules.add(rule)

