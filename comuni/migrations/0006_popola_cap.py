import csv
import os

from django.db import migrations


# noinspection PyUnusedLocal
def forwards_func(apps, schema_editor):
    comuni = apps.get_model("comuni", "Comune")
    datapath = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'fixtures')
    with open(os.path.join(datapath, 'listacomuni.txt'),
              encoding='iso-8859-1') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';')
        print("")
        for row in spamreader:
            if row[0] == 'Istat':
                continue
            if len(row[0]) > 1:
                comune = comuni.objects.filter(codice_istat=row[0]).first()
                if comune:
                    comune.cap = row[5]
                    comune.save()
                    print(f"Cap Aggiornato {comune.nome} - {row[5]}")
                else:
                    # provo col nome
                    comune = comuni.objects.filter(nome=row[1]).first()
                    if comune:
                        comune.cap = row[5]
                        comune.save()
                        print(f"Cap Aggiornato {comune.nome} - {row[5]}")
                        continue
                    # provo con l'inizio del nome
                    comune = comuni.objects.filter(nome__startswith=row[1]).first()
                    if comune:
                        comune.cap = row[5]
                        if comune.provincia.sigla == '-':
                            # correggo sigla provincia
                            comune.provincia.sigla = row[2]
                            comune.provincia.save()
                        comune.save()
                        print(f"Cap Aggiornato {comune.nome} - {row[5]}")


# noinspection PyUnusedLocal
def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('comuni', '0005_popola_comuni'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func)
    ]
