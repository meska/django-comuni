import csv
import os

from django.db import migrations


# noinspection PyUnusedLocal
def forwards_func(apps, schema_editor):
    comuni = apps.get_model("comuni", "Comune")
    province = apps.get_model("comuni", "Provincia")
    ripartizioni = apps.get_model("comuni", "RipartizioneGeografica")
    datapath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fixtures')
    with open(os.path.join(datapath, 'Elenco-comuni-italiani.csv'),
              encoding='iso-8859-1') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        print("")
        for row in spamreader:
            if row[0] == 'Codice Regione':
                continue
            if len(row[5]) > 0:
                prov = province.objects.filter(sigla=row[13]).first()
                rip = ripartizioni.objects.filter(codice=row[7]).first()
                reg, created = comuni.objects.get_or_create(
                    provincia=prov,
                    ripartizione=rip,
                    codice_istat=row[4],
                    codice_catastale=row[18],
                    nome=row[5],
                    nome_de=row[6],
                    capoluogo=True if row[12] == '1' else False,
                )
                if created:
                    print(f"Inserito {row[5]}")

        # aggiorno sigla per nuova provincia Sud Sardegna
        province.objects.filter(nome='Sud Sardegna').update(sigla='SU')


# noinspection PyUnusedLocal
def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('comuni', '0004_popola_aree'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func)
    ]
