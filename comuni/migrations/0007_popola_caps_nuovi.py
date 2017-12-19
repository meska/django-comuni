import csv
import os

from django.db import migrations


# noinspection PyUnusedLocal
def forwards_func(apps, schema_editor):
    comuni = apps.get_model("comuni", "Comune")
    datapath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fixtures')
    with open(os.path.join(datapath, 'caps_nuovi.txt')) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        print("")
        for row in spamreader:
            if len(row[0]) > 1:
                comune = comuni.objects.filter(codice_istat=row[0]).first()
                if comune:
                    comune.cap = row[4]
                    comune.save()
                    print(f"Cap Aggiornato {comune.nome} - {row[4]}")


# noinspection PyUnusedLocal
def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('comuni', '0006_popola_cap'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func)
    ]
