# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-17 11:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('identifier', models.TextField()),
                ('parameter_miejsce_badania', models.TextField(default='')),
                ('parameter_rocznik', models.FloatField()),
                ('parameter_wyznanie', models.TextField(default='')),
                ('parameter_jezyk', models.TextField(default='')),
                ('parameter_powiat_urodzenia', models.TextField(default='')),
                ('parameter_waga', models.FloatField()),
                ('parameter_wzrost', models.FloatField()),
                ('parameter_wzrost_od_ziemi_do_podbrodka', models.FloatField()),
                ('parameter_wzrost_od_ziemi_do_mostka', models.FloatField()),
                ('parameter_wzrost_do_wzgorka_lonowego', models.FloatField()),
                ('parameter_wzrost_do_kolan', models.FloatField()),
                ('parameter_wzrost_do_kostki', models.FloatField()),
                ('parameter_wzrost_od_ziemi_do_ramienia', models.FloatField()),
                ('parameter_od_ziemi_do_lokcia', models.FloatField()),
                ('parameter_od_ziemi_do_nadgarstka', models.FloatField()),
                ('parameter_od_ziemi_do_konca_palca_srodkowego', models.FloatField()),
                ('parameter_dlugosc_stopy_od_piety_do_duzego_palca_u_nogi', models.FloatField()),
                ('parameter_szerokosc_stopy', models.FloatField()),
                ('parameter_szerokosc_w_barkach', models.FloatField()),
                ('parameter_szerokosc_klatki_piersiowej', models.FloatField()),
                ('parameter_glebokosc_klatki_piersiowej', models.FloatField()),
                ('parameter_szerokosc_w_biodrach', models.FloatField()),
                ('parameter_szerokosc_dloni', models.FloatField()),
                ('parametr_dlugosc_palca_srodkowego', models.FloatField()),
                ('parametr_wysokosc_twarzy_od_brody_do_poziomu_oczu', models.FloatField()),
                ('parameter_od_oczu_do_gornej_szczeki', models.FloatField()),
                ('parameter_wysokosc_nosa', models.FloatField()),
                ('parameter_szerokosc_nosa_u_podstawy', models.FloatField()),
                ('parameter_dlugosc_czaszki_od_czola_do_potylicy', models.FloatField()),
                ('parameter_szerokosc_czaszki_na_wysokosci_oczu', models.FloatField()),
                ('parameter_szerokosc_czaszki_na_wysokosci_uszu', models.FloatField()),
                ('szerokosc_czola', models.FloatField()),
                ('szerokosc_twarzy', models.FloatField()),
                ('szerokosc_zuchwy', models.FloatField()),
                ('obwod_glowy', models.FloatField()),
                ('obwod_szyi', models.FloatField()),
                ('obwod_piersi', models.FloatField()),
                ('obwod_w_pasie', models.FloatField()),
                ('obwod_bioder', models.FloatField()),
                ('obwod_posladkow', models.FloatField()),
                ('najwiekszy_obwod_ramienia', models.FloatField()),
                ('najwiekszy_obwod_przedramienia', models.FloatField()),
                ('najmniejszy_obwod_przedramienia', models.FloatField()),
                ('najwiekszy_obwod_uda', models.FloatField()),
                ('parameter_obwod_kolana', models.FloatField()),
                ('parameter_najwiekszy_obwod_przedudzia', models.FloatField()),
                ('parameter_najmniejszy_obwod_przedudzia', models.FloatField()),
                ('parameter_obwod_podbicia_gornego', models.FloatField()),
                ('parameter_obwod_podbicia_dolnego', models.FloatField()),
            ],
        ),
    ]
