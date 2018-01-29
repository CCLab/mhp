import csv
import os

from django.core.files import File
from django.conf import settings
from django.core.management.base import BaseCommand

import pyexifinfo

from src.apps.parametrizedimage.models import CardImage, CardImageTag, CARD_PARAMETERS
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
        CardImage.objects.all().delete()
        CardImageTag.objects.all().delete()

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

                found = False
                for card_parameter in CARD_PARAMETERS:
                    if 'csv_field_name' in card_parameter and card_parameter['csv_field_name'] == name:
                        found = True

                if not found:
                    print("Heading column not found in CSV file: %s" % name)

            for item in reader:
                identifier = item[column_ids[IDENTIFIER_COLUMN]] \
                    .replace(' ', '') \
                    .replace('\xa0', '')

                card_directory_name = 'Karta_%05d' % int(identifier)

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
                elif len(jpeg_file_names) > 2:
                    assert(False)

                pdf_file_cache = None

                pdf_path = os.path.join(
                    card_container_directory,
                    reverse_card_location_dictionary[card_directory_name],
                    card_directory_name,
                    'PDF')

                i = 0
                for jpeg_file_name in jpeg_file_names:
                    i += 1
                    card_image = CardImage()
                    card_image.card_id = int(identifier)
                    card_image.image_id = i

                    card_image.image.save(
                        '%s.jpg' % identifier,
                        File(open(downscale_image(os.path.join(jpeg_path, jpeg_file_name)), 'rb')))

                    exif_json = pyexifinfo.get_json(os.path.join(jpeg_path, jpeg_file_name))
                    assert len(exif_json) == 1
                    exif_json = exif_json[0]

                    pdf_file_names = os.listdir(pdf_path)
                    if len(pdf_file_names) < 1:
                        pass
                    elif len(pdf_file_names) == 1:
                        if pdf_file_cache:
                            card_image.pdf_file = pdf_file_cache
                        else:
                            card_image.pdf_file.save(
                                '%s.pdf' % identifier,
                                File(open(os.path.join(pdf_path, pdf_file_names[0]), 'rb')))
                            pdf_file_cache = card_image.pdf_file

                    elif len(pdf_file_names) > 1:
                        assert(False)

                    for card_parameter in CARD_PARAMETERS:
                        if 'csv_field_name' in card_parameter:
                            column_id = column_ids[card_parameter['csv_field_name']]
                            parameter_attribute_name = card_parameter['parameter_name']

                            if card_parameter['type'] == 'float':
                                parameter_value = item[column_id]
                                parameter_value = parameter_value.replace('\xa0', '')
                                parameter_value = parameter_value.replace(',', '.')
                                parameter_value = parameter_value.strip()

                                if parameter_value == '':
                                    parameter_value = 0.0

                                setattr(card_image, parameter_attribute_name, parameter_value)
                            elif card_parameter['type'] == 'string':
                                parameter_value = item[column_id]
                                setattr(card_image, parameter_attribute_name, parameter_value)
                            else:
                                assert(False)
                        elif 'exif_field_name' in card_parameter:
                            value = exif_json[card_parameter['exif_field_name']]

                            if card_parameter['type'] == 'string':
                                parameter_attribute_name = card_parameter['parameter_name']
                                setattr(card_image, parameter_attribute_name, value)
                            elif card_parameter['type'] == 'tags':
                                for tag in value.split(';'):
                                    tag = tag.strip()
                                    tag_object, unused_created = CardImageTag.objects.get_or_create(name=tag)
                                    tag_object.card_images.add(card_image)
                                    tag_object.save()
                            else:
                                assert(False)
                    card_image.save()
