import csv
import os

from django.db import migrations


# noinspection PyUnusedLocal
def forwards_func(apps, schema_editor):
    province = apps.get_model("comuni", "Provincia")
    regioni = apps.get_model("comuni", "Regione")
    datapath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fixtures')
    with open(os.path.join(datapath, 'Elenco-comuni-italiani.csv'),
              encoding='iso-8859-1') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        print("")
        for row in spamreader:
            if row[0] == 'Codice Regione':
                continue
            if len(row[2]) > 0 and len(row[13]) and (len(row[10]) > 1 or len(row[11]) > 1):
                if len(row[10]) > 1:
                    nomi = row[10].split("/")
                if len(row[11]) > 1:
                    nomi = row[11].split("/")

                if len(nomi) == 1:
                    reg, created = province.objects.get_or_create(
                        codice=row[2],
                        sigla=row[13],
                        nome=nomi[0],
                        regione=regioni.objects.get(codice=row[0])
                    )
                    if created:
                        print(f"Inserita {nomi[0]}")
                if len(nomi) > 1:
                    reg, created = province.objects.get_or_create(
                        codice=row[2],
                        sigla=row[13],
                        nome=nomi[0],
                        nome_de=nomi[1],
                        regione=regioni.objects.get(codice=row[0])
                    )
                    if created:
                        print(f"Inserita {nomi[0]}")




# noinspection PyUnusedLocal
def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('comuni', '0002_popola_regioni'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func)
    ]
