from django.db import models


CARD_PARAMETERS = [
    {
        'csv_field_name': 'miejsce badania',
        'parameter_name': 'parameter_miejsce_badania',
        'type': 'string',
    },
    {
        'csv_field_name': 'rocznik',
        'parameter_name': 'parameter_rocznik',
        'type': 'float',
    },
    {
        'csv_field_name': 'wyznanie',
        'parameter_name': 'parameter_wyznanie',
        'type': 'string',
    },
    {
        'csv_field_name': 'jezyk',
        'parameter_name': 'parameter_jezyk',
        'type': 'string',
    },
    {
        'csv_field_name': 'powiat urodzenia',
        'parameter_name': 'parameter_powiat_urodzenia',
        'type': 'string',
    },
    {
        'csv_field_name': 'waga',
        'parameter_name': 'parameter_waga',
        'type': 'float',
    },
    {
        'csv_field_name': 'wzrost',
        'parameter_name': 'parameter_wzrost',
        'type': 'float',
    },
    {
        'csv_field_name': 'gnathion',
        'parameter_name': 'parameter_wzrost_od_ziemi_do_podbrodka',
        'type': 'float',
    },
    {
        'csv_field_name': 'suprasternale',
        'parameter_name': 'parameter_wzrost_od_ziemi_do_mostka',
        'type': 'float',
    },
    {
        'csv_field_name': 'symphysion',
        'parameter_name': 'parameter_wzrost_do_wzgorka_lonowego',
        'type': 'float',
    },
    {
        'csv_field_name': 'tibiale',
        'parameter_name': 'parameter_wzrost_do_kolan',
        'type': 'float',
    },
    {
        'csv_field_name': 'sphyrion',
        'parameter_name': 'parameter_wzrost_do_kostki',
        'type': 'float',
    },
    {
        'csv_field_name': 'akromion',
        'parameter_name': 'parameter_wzrost_od_ziemi_do_ramienia',
        'type': 'float',
    },
    {
        'csv_field_name': 'radiale',
        'parameter_name': 'parameter_od_ziemi_do_lokcia',
        'type': 'float',
    },
    {
        'csv_field_name': 'stylion',
        'parameter_name': 'parameter_od_ziemi_do_nadgarstka',
        'type': 'float',
    },
    {
        'csv_field_name': 'daktylion',
        'parameter_name': 'parameter_od_ziemi_do_konca_palca_srodkowego',
        'type': 'float',
    },
    {
        'csv_field_name': 'pterion-akrop(odion).',
        'parameter_name': 'parameter_dlugosc_stopy_od_piety_do_duzego_palca_u_nogi',
        'type': 'float',
    },
    {
        'csv_field_name': 'Mtr. I,-mtr. m.',
        'parameter_name': 'parameter_szerokosc_stopy',
        'type': 'float',
    },
    {
        'csv_field_name': 'Akrom-Akrom',
        'parameter_name': 'parameter_szerokosc_w_barkach',
        'type': 'float',
    },
    {
        'csv_field_name': 'Śr. piers. poprz.',
        'parameter_name': 'parameter_szerokosc_klatki_piersiowej',
        'type': 'float',
    },
    {
        'csv_field_name': 'Śr. piers. strz.',
        'parameter_name': 'parameter_glebokosc_klatki_piersiowej',
        'type': 'float',
    },
    {
        'csv_field_name': 'Iliocrist.-illiocr.',
        'parameter_name': 'parameter_szerokosc_w_biodrach',
        'type': 'float',
    },
    {
        'csv_field_name': 'Iliocrist.-illiocr.',
        'parameter_name': 'parameter_szerokosc_w_biodrach',
        'type': 'float',
    },
    {
        'csv_field_name': 'Metacar. l.-met. m.',
        'parameter_name': 'parameter_szerokosc_dloni',
        'type': 'float',
    },
    {
        'csv_field_name': 'Phal(angion)III-Dakt.',
        'parameter_name': 'parametr_dlugosc_palca_srodkowego',
        'type': 'float',
    },
    {
        'csv_field_name': 'Nasion.-Gnath.',
        'parameter_name': 'parametr_wysokosc_twarzy_od_brody_do_poziomu_oczu',
        'type': 'float',
    },
    {
        'csv_field_name': 'Nas.-Prosth.',
        'parameter_name': 'parameter_od_oczu_do_gornej_szczeki',
        'type': 'float',
    },
    {
        'csv_field_name': 'Nas.-Subnas.',
        'parameter_name': 'parameter_wysokosc_nosa',
        'type': 'float',
    },
    {
        'csv_field_name': 'Alare.-Alare.',
        'parameter_name': 'parameter_szerokosc_nosa_u_podstawy',
        'type': 'float',
    },
    {
        'csv_field_name': 'Glab.-Opist.',
        'parameter_name': 'parameter_dlugosc_czaszki_od_czola_do_potylicy',
        'type': 'float',
    },
    {
        'csv_field_name': 'Eur.-Eur.',
        'parameter_name': 'parameter_szerokosc_czaszki_na_wysokosci_oczu',
        'type': 'float',
    },
    {
        'csv_field_name': 'Mast.-Mast.',
        'parameter_name': 'parameter_szerokosc_czaszki_na_wysokosci_uszu',
        'type': 'float',
    },
]

class Card(models.Model):
    image = models.ImageField()
    identifier = models.TextField()

    for parameter in CARD_PARAMETERS:
        if parameter['type'] == 'float':
            locals()[parameter['parameter_name']] = models.FloatField()
        elif parameter['type'] == 'string':
            locals()[parameter['parameter_name']] = models.TextField(default='')
        else:
            assert(False)
