import csv
import os

from django.db import migrations


# noinspection PyUnusedLocal
def forwards_func(apps, schema_editor):
    regione = apps.get_model("comuni", "Regione")
    datapath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fixtures')
    with open(os.path.join(datapath, 'Elenco-comuni-italiani.csv'),
              encoding='iso-8859-1') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        print("")
        for row in spamreader:
            if row[0] == 'Codice Regione':
                continue
            if len(row[0]) > 0 and len(row[9]) > 0:
                nomi = row[9].split("/")
                if len(nomi) == 1:
                    reg, created = regione.objects.get_or_create(codice=row[0], nome=nomi[0])
                    if created:
                        print(f"Inserita {nomi[0]}")
                if len(nomi) > 1:
                    reg, created = regione.objects.get_or_create(codice=row[0], nome=nomi[0], nome_de=nomi[1])
                    if created:
                        print(f"Inserita {nomi[0]}")


# noinspection PyUnusedLocal
def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('comuni', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func)
    ]
