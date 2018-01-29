from django.db import models


CARD_PARAMETERS = [
    {
        'csv_field_name': 'miejsce badania',
        'parameter_name': 'parameter_miejsce_badania',
        'parameter_name_human': 'Miejsce badania',
        'type': 'string',
        'more_important': True,
    },
    {
        'csv_field_name': 'data badania',
        'parameter_name': 'parameter_data_badania',
        'parameter_name_human': 'Data badania',
        'type': 'string',
        'more_important': True,
    },
    {
        'csv_field_name': 'rocznik',
        'parameter_name': 'parameter_rocznik',
        'parameter_name_human': 'Rocznik',
        'type': 'float',
        'more_important': True,
    },
    {
        'csv_field_name': 'wyznanie',
        'parameter_name': 'parameter_wyznanie',
        'parameter_name_human': 'Wyznanie',
        'type': 'string',
        'more_important': True,
    },
    {
        'csv_field_name': 'jezyk',
        'parameter_name': 'parameter_jezyk',
        'parameter_name_human': 'Język',
        'type': 'string',
        'more_important': True,
    },
    {
        'csv_field_name': 'powiat urodzenia',
        'parameter_name': 'parameter_powiat_urodzenia',
        'parameter_name_human': 'Powiat urodzenia',
        'type': 'string',
        'more_important': True,
    },
    {
        'csv_field_name': 'waga',
        'parameter_name': 'parameter_waga',
        'parameter_name_human': 'Waga',
        'type': 'float',
        'more_important': True,
    },
    {
        'csv_field_name': 'wzrost',
        'parameter_name': 'parameter_wzrost',
        'parameter_name_human': 'Wzrost',
        'type': 'float',
        'more_important': True,
    },
    {
        'csv_field_name': 'gnathion',
        'parameter_name': 'parameter_wzrost_od_ziemi_do_podbrodka',
        'parameter_name_human': 'Wzrost od ziemi do podbródka',
        'type': 'float',
        'more_important': False,
    },
    {
        'csv_field_name': 'suprasternale',
        'parameter_name': 'parameter_wzrost_od_ziemi_do_mostka',
        'parameter_name_human': 'Wzrost od ziemi do mostka',
        'type': 'float',
        'more_important': False,
    },
    {
        'csv_field_name': 'symphysion',
        'parameter_name': 'parameter_wzrost_do_wzgorka_lonowego',
        'parameter_name_human': 'Wzrost od ziemi do wzgórka łonowego',
        'type': 'float',
        'more_important': False,
    },
    {
        'csv_field_name': 'tibiale',
        'parameter_name': 'parameter_wzrost_do_kolan',
        'parameter_name_human': 'Wzrost do kolan',
        'type': 'float',
        'more_important': False,
    },
    {
        'csv_field_name': 'sphyrion',
        'parameter_name': 'parameter_wzrost_do_kostki',
        'parameter_name_human': 'Wzrost do kostki',
        'type': 'float',
        'more_important': False,
    },
    {
        'csv_field_name': 'akromion',
        'parameter_name': 'parameter_wzrost_od_ziemi_do_ramienia',
        'parameter_name_human': 'Wzrost od ziemi do ramienia',
        'type': 'float',
        'more_important': False,
    },
    {
        'csv_field_name': 'radiale',
        'parameter_name': 'parameter_od_ziemi_do_lokcia',
        'parameter_name_human': 'Wzrost od ziemi do łokcia',
        'type': 'float',
        'more_important': False,
    },
    {
        'csv_field_name': 'stylion',
        'parameter_name': 'parameter_od_ziemi_do_nadgarstka',
        'parameter_name_human': 'Wzrost od ziemi do nadgarstka',
        'type': 'float',
        'more_important': False,
    },
    {
        'csv_field_name': 'daktylion',
        'parameter_name': 'parameter_od_ziemi_do_konca_palca_srodkowego',
        'parameter_name_human': 'Wzrost od ziemi do końca palca środkowego',
        'type': 'float',
        'more_important': False,
    },
    {
        'csv_field_name': 'pterion-akrop(odion).',
        'parameter_name': 'parameter_dlugosc_stopy_od_piety_do_duzego_palca_u_nogi',
        'parameter_name_human': 'Długość stopy od pięty do dużego palca u nogi',
        'type': 'float',
        'more_important': False,
    },
    {
        'csv_field_name': 'Mtr. I,-mtr. m.',
        'parameter_name': 'parameter_szerokosc_stopy',
        'parameter_name_human': 'Szerokość stopy',
        'type': 'float',
        'more_important': False,
    },
    {
        'csv_field_name': 'Akrom-Akrom',
        'parameter_name': 'parameter_szerokosc_w_barkach',
        'parameter_name_human': 'Szerokość w barkach',
        'type': 'float',
        'more_important': False,
    },
    {
        'csv_field_name': 'Śr. piers. poprz.',
        'parameter_name': 'parameter_szerokosc_klatki_piersiowej',
        'parameter_name_human': 'Szerokość klatki piersiowej',
        'type': 'float',
        'more_important': False,
    },
    {
        'csv_field_name': 'Śr. piers. strz.',
        'parameter_name': 'parameter_glebokosc_klatki_piersiowej',
        'parameter_name_human': 'Głębokość klatki piersiowej',
        'type': 'float',
        'more_important': False,
    },
    {
        'csv_field_name': 'Iliocrist.-illiocr.',
        'parameter_name': 'parameter_szerokosc_w_biodrach',
        'parameter_name_human': 'Szerokość w biodrach',
        'type': 'float',
        'more_important': False,
    },
    {
        'csv_field_name': 'Metacar. l.-met. m.',
        'parameter_name': 'parameter_szerokosc_dloni',
        'parameter_name_human': 'Szerokość dłoni',
        'type': 'float',
        'more_important': False,
    },
    {
        'csv_field_name': 'Phal(angion)III-Dakt.',
        'parameter_name': 'parametr_dlugosc_palca_srodkowego',
        'parameter_name_human': 'Długość palca środkowego',
        'type': 'float',
        'more_important': False,
    },
    {
        'csv_field_name': 'Nasion.-Gnath.',
        'parameter_name': 'parametr_wysokosc_twarzy_od_brody_do_poziomu_oczu',
        'parameter_name_human': 'Wysokość twarzy od brody do poziomu oczu',
        'type': 'float',
        'more_important': False,
    },
    {
        'csv_field_name': 'Nas.-Prosth.',
        'parameter_name': 'parameter_od_oczu_do_gornej_szczeki',
        'parameter_name_human': 'Odległość od oczu do górnej szczęki',
        'type': 'float',
        'more_important': False,
    },
    {
        'csv_field_name': 'Nas.-Subnas.',
        'parameter_name': 'parameter_wysokosc_nosa',
        'parameter_name_human': 'Wysokość nosa',
        'type': 'float',
        'more_important': False,
    },
    {
        'csv_field_name': 'Alare.-Alare.',
        'parameter_name': 'parameter_szerokosc_nosa_u_podstawy',
        'parameter_name_human': 'Szerokość nosa u podstawy',
        'type': 'float',
        'more_important': False,
    },
    {
        'csv_field_name': 'Glab.-Opist.',
        'parameter_name': 'parameter_dlugosc_czaszki_od_czola_do_potylicy',
        'parameter_name_human': 'Długość czaszki od czoła do potylicy',
        'type': 'float',
        'more_important': False,
    },
    {
        'csv_field_name': 'Eur.-Eur.',
        'parameter_name': 'parameter_szerokosc_czaszki_na_wysokosci_oczu',
        'parameter_name_human': 'Szerokość czaszki na wysokości oczu',
        'type': 'float',
        'more_important': False,
    },
    {
        'csv_field_name': 'Mast.-Mast.',
        'parameter_name': 'parameter_szerokosc_czaszki_na_wysokosci_uszu',
        'parameter_name_human': 'Szerokość czaszki na wysokości uszu',
        'type': 'float',
        'more_important': False,
    },
    {
        'csv_field_name': 'Front.-Front.',
        'parameter_name': 'szerokosc_czola',
        'parameter_name_human': 'Szerokość czoła',
        'type': 'float',
        'more_important': False,
    },
    {
        'csv_field_name': 'Zyg.-Zyg.',
        'parameter_name': 'szerokosc_twarzy',
        'parameter_name_human': 'Szerokość twarzy',
        'type': 'float',
        'more_important': False,
    },
    {
        'csv_field_name': 'Gon.-Gon.',
        'parameter_name': 'szerokosc_zuchwy',
        'parameter_name_human': 'Szerokość żuchwy',
        'type': 'float',
        'more_important': False,
    },
    {
        'csv_field_name': 'Ob. Głowy',
        'parameter_name': 'obwod_glowy',
        'parameter_name_human': 'Obwód głowy',
        'type': 'float',
        'more_important': False,
    },
    {
        'csv_field_name': 'Ob. szyi',
        'parameter_name': 'obwod_szyi',
        'parameter_name_human': 'Obwód szyi',
        'type': 'float',
        'more_important': False,
    },
    {
        'csv_field_name': 'Ob. Piersi',
        'parameter_name': 'obwod_piersi',
        'parameter_name_human': 'Obwód piersi',
        'type': 'float',
        'more_important': False,
    },
    {
        'csv_field_name': 'Ob. w pasie',
        'parameter_name': 'obwod_w_pasie',
        'parameter_name_human': 'Obwód w pasie',
        'type': 'float',
        'more_important': False,
    },
    {
        'csv_field_name': 'Ob. na lliosp.',
        'parameter_name': 'obwod_bioder',
        'parameter_name_human': 'Obwód bioder',
        'type': 'float',
        'more_important': False,
    },
    {
        'csv_field_name': 'Ob. na Trochan.',
        'parameter_name': 'obwod_posladkow',
        'parameter_name_human': 'Obwód pośladków',
        'type': 'float',
        'more_important': False,
    },
    {
        'csv_field_name': 'Najw. ob. ram.',
        'parameter_name': 'najwiekszy_obwod_ramienia',
        'parameter_name_human': 'Największy obwód ramienia',
        'type': 'float',
        'more_important': False,
    },
    {
        'csv_field_name': 'Najw. ob. przedr.',
        'parameter_name': 'najwiekszy_obwod_przedramienia',
        'parameter_name_human': 'Największy obwód przedramienia',
        'type': 'float',
        'more_important': False,
    },
    {
        'csv_field_name': 'Najm. ob. przedr.',
        'parameter_name': 'najmniejszy_obwod_przedramienia',
        'parameter_name_human': 'Najmniejszy obwód przedramienia',
        'type': 'float',
        'more_important': False,
    },
    {
        'csv_field_name': 'Najw. ob. Uda',
        'parameter_name': 'najwiekszy_obwod_uda',
        'parameter_name_human': 'Największy obwód uda',
        'type': 'float',
        'more_important': False,
    },
    {
        'csv_field_name': 'Ob. Kolana',
        'parameter_name': 'parameter_obwod_kolana',
        'parameter_name_human': 'Obwód kolana',
        'type': 'float',
        'more_important': False,
    },
    {
        'csv_field_name': 'Najw. ob. przedudzi.',
        'parameter_name': 'parameter_najwiekszy_obwod_przedudzia',
        'parameter_name_human': 'Największy obwód przedudzia',
        'type': 'float',
        'more_important': False,
    },
    {
        'csv_field_name': 'Najmn. ob. przedudzi.',
        'parameter_name': 'parameter_najmniejszy_obwod_przedudzia',
        'parameter_name_human': 'Najmniejszy obwód przedudzia',
        'type': 'float',
        'more_important': False,
    },
    {
        'csv_field_name': 'Ob. podbicia górn.',
        'parameter_name': 'parameter_obwod_podbicia_gornego',
        'parameter_name_human': 'Obwód podbicia górnego',
        'type': 'float',
        'more_important': False,
    },
    {
        'csv_field_name': 'Ob. podbicia doln.',
        'parameter_name': 'parameter_obwod_podbicia_dolnego',
        'parameter_name_human': 'Obwód podbicia dolnego',
        'type': 'float',
        'more_important': False,
    },
    {
        'exif_field_name': 'XMP:Creator',
        'parameter_name': 'instytucja',
        'parameter_name_human': "Instytucja",
        'type': 'string',
        'more_important': True,
    },
    {
        'exif_field_name': 'EXIF:XPKeywords',
        'type': 'tags',
        'parameter_name': "tags",
        'parameter_name_human': "Tagi",
        'more_important': True,
    }
]


class CardImage(models.Model):
    class Meta:
        ordering = ['card_id', 'image_id']
    pdf_file = models.FileField()
    card_id = models.IntegerField(db_index=True)
    image_id = models.IntegerField(db_index=True)
    image = models.ImageField()

    for parameter in CARD_PARAMETERS:
        if parameter['type'] == 'float':
            locals()[parameter['parameter_name']] = models.FloatField(null=True, blank=True, db_index=True)
        elif parameter['type'] == 'string':
            locals()[parameter['parameter_name']] = models.TextField(default='', db_index=True)
        elif parameter['type'] == 'tags':
            # such a m2m field already exists on CardImageTag
            pass
        else:
            assert(False)

    def get_parameter_value_dictionary(self):
        result = []
        for parameter in CARD_PARAMETERS:
            if parameter['type'] == 'string':
                value = getattr(self, parameter['parameter_name'])
                result.append((parameter['parameter_name_human'], value))
            elif parameter['type'] == 'float':
                value = getattr(self, parameter['parameter_name'])
                value = '%.0f' % value
                result.append((parameter['parameter_name_human'], value))
            elif parameter['type'] == 'tags':
                value = ', '.join([tag.name for tag in self.cardimagetag_set.all()])
                result.append((parameter['parameter_name_human'], value))

        return result

    def get_parameter_value_dictionary_more_important(self):
        values = dict(self.get_parameter_value_dictionary())
        result = []

        for parameter in CARD_PARAMETERS:
            if parameter['more_important']:
                result.append((parameter['parameter_name_human'], values[parameter['parameter_name_human']]))
        return result

    def get_parameter_value_dictionary_part_1(self):
        values = self.get_parameter_value_dictionary()
        return values[:int(len(values) / 2) + 1]

    def get_parameter_value_dictionary_part_2(self):
        values = self.get_parameter_value_dictionary()
        return values[int(len(values) / 2) + 1:]

    def get_previous_card_image_pk(self):
        if self.image_id == 2:
            return CardImage.objects.get(card_id=self.card_id, image_id=1).pk
        elif self.image_id == 1:
            objects = CardImage.objects.filter(card_id__lt=self.card_id).order_by('-card_id', '-image_id')

            if len(objects) > 0:
                return objects[0].pk
            else:
                return None
        else:
            assert(False)

    def get_next_card_image_pk(self):
        if self.image_id == 2:
            objects = CardImage.objects.filter(card_id__gt=self.card_id).order_by('card_id', 'image_id')

            if len(objects) > 0:
                return objects[0].pk
            else:
                return None
        elif self.image_id == 1:
            try:
                return CardImage.objects.get(card_id=self.card_id, image_id=2).pk
            except CardImage.DoesNotExist:
                objects = (CardImage
                           .objects
                           .filter(card_id__gt=self.card_id)
                           .order_by('card_id', 'image_id'))
                if len(objects) > 0:
                    return objects[0].pk
                else:
                    return None
        else:
            assert(False)


class CardImageTag(models.Model):
    name = models.TextField(db_index=True)
    card_images = models.ManyToManyField(CardImage)
