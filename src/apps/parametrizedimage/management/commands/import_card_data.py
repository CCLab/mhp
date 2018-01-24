import csv
import os

from django.core.files import File
from django.conf import settings
from django.core.management.base import BaseCommand

from src.apps.parametrizedimage.models import Card, CARD_PARAMETERS
from src.utils import downscale_image

DATA_FILE_NAME = str(settings.BASE_DIR.path('data', 'cards.csv'))
IDENTIFIER_COLUMN = 'karta'


class Command(BaseCommand):
    '''
    import card data
    '''

    def add_arguments(self, parser):
        parser.add_argument(
            '--data-directory',
            required=True,
            help='Data directory')

    def handle(self, *args, **options):
        Card.objects.all().delete()

        data_directory = options['data_directory']

        reverse_card_location_dictionary = {}

        card_container_directory = os.path.join(data_directory, 'Kultura_Cyfrowa', 'Karty_pomiarowe')
        for container_directory_name in os.listdir(card_container_directory):
            if 'Karton' not in container_directory_name:
                continue

            for card_directory_name in os.listdir(os.path.join(card_container_directory, container_directory_name)):
                if os.path.exists(os.path.join(
                        card_container_directory,
                        container_directory_name,
                        card_directory_name,
                        'JPEG')):
                    reverse_card_location_dictionary[card_directory_name] = container_directory_name

        with open(DATA_FILE_NAME) as csv_file:
            column_ids = {}

            reader = csv.reader(csv_file, quotechar='"')
            header = next(reader)

            for i, name in enumerate(header):
                column_ids[name] = i

            for item in reader:
                identifier = item[column_ids[IDENTIFIER_COLUMN]] \
                    .replace(' ', '') \
                    .replace('\xa0', '')

                Card.objects.filter(identifier=identifier).delete()

                card = Card()
                card.identifier = identifier

                card_directory_name = 'Karta_%05d' % int(card.identifier)

                if card_directory_name not in reverse_card_location_dictionary:
                    print("No JPEG folder for card %s, ignoring..." % identifier)
                    continue

                jpeg_path = os.path.join(
                    card_container_directory,
                    reverse_card_location_dictionary[card_directory_name],
                    card_directory_name,
                    'JPEG')

                jpeg_file_names = os.listdir(jpeg_path)
                if len(jpeg_file_names) < 1:
                    print("Empty JPEG folder for card %s, ignoring..." % identifier)
                    continue
                elif len(jpeg_file_names) in [1, 2]:
                    card.image1.save(
                        jpeg_file_names[0],
                        File(open(downscale_image(os.path.join(jpeg_path, jpeg_file_names[0])), 'rb')))

                    if len(jpeg_file_names) == 2:
                        card.image2.save(
                            jpeg_file_names[1],
                            File(open(downscale_image(os.path.join(jpeg_path, jpeg_file_names[1])), 'rb')))
                elif len(jpeg_file_names) > 2:
                    assert(False)

                for card_parameter in CARD_PARAMETERS:
                    column_id = column_ids[card_parameter['csv_field_name']]
                    parameter_attribute_name = card_parameter['parameter_name']

                    if card_parameter['type'] == 'float':
                        parameter_value = item[column_id]
                        parameter_value = parameter_value.replace('\xa0', '')
                        parameter_value = parameter_value.replace(',', '.')
                        parameter_value = parameter_value.strip()

                        if parameter_value == '':
                            parameter_value = 0.0

                        setattr(card, parameter_attribute_name, parameter_value)
                    elif card_parameter['type'] == 'string':
                        parameter_value = item[column_id]
                        setattr(card, parameter_attribute_name, parameter_value)
                    else:
                        assert(False)

                card.save()
