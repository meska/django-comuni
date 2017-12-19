import csv
import os

from django.db import migrations


# noinspection PyUnusedLocal
def forwards_func(apps, schema_editor):
    ripartizione = apps.get_model("comuni", "RipartizioneGeografica")
    datapath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fixtures')
    with open(os.path.join(datapath, 'Elenco-comuni-italiani.csv'),
              encoding='iso-8859-1') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        print("")
        for row in spamreader:
            if row[0] == 'Codice Regione':
                continue
            if len(row[7]) > 0 and len(row[8]):
                reg, created = ripartizione.objects.get_or_create(
                    codice=row[7],
                    nome=row[8],
                )
                if created:
                    print(f"Inserita {row[8]}")


# noinspection PyUnusedLocal
def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('comuni', '0003_popola_province'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func)
    ]
