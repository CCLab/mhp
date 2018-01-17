import csv

from django.conf import settings
from django.core.management.base import BaseCommand

from src.apps.parametrizedimage.models import Card, CARD_PARAMETERS

DATA_FILE_NAME = str(settings.BASE_DIR.path('data', 'baza_danych_dla_kart_00001-15000.csv'))
IDENTIFIER_COLUMN = 'karta'


class Command(BaseCommand):
    '''
    import card data
    '''

    def handle(self, *args, **kwargs):
        with open(DATA_FILE_NAME) as csv_file:
            column_ids = {}

            reader = csv.reader(csv_file, quotechar='"')
            header = next(reader)

            for i, name in enumerate(header):
                column_ids[name] = i

            for item in reader:
                identifier = item[column_ids[IDENTIFIER_COLUMN]]

                Card.objects.filter(identifier=identifier).delete()

                card = Card()
                card.identifier = identifier
                card.image = str(settings.BASE_DIR.path('cards', '%s.jpg' % identifier))

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
