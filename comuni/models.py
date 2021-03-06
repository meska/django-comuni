from django.db import models
from django.db.models import PROTECT


class Regione(models.Model):
    codice = models.CharField(max_length=5, unique=True, db_index=True)
    nome = models.CharField(max_length=100, db_index=True)
    nome_de = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ('nome',)
        verbose_name = "Regione"
        verbose_name_plural = "Regioni"


class RipartizioneGeografica(models.Model):
    codice = models.CharField(max_length=5, unique=True, db_index=True)
    nome = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ('nome',)
        verbose_name = "Ripartizione"
        verbose_name_plural = "Ripartizioni"


class Provincia(models.Model):
    codice = models.CharField(max_length=5, unique=True, db_index=True)
    sigla = models.CharField(max_length=5)
    nome = models.CharField(max_length=50, db_index=True)
    nome_de = models.CharField(max_length=50, null=True, blank=True)
    regione = models.ForeignKey(Regione, on_delete=PROTECT)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ('nome',)
        verbose_name = "Provincia"
        verbose_name_plural = "Province"


class Comune(models.Model):
    provincia = models.ForeignKey(Provincia)
    ripartizione = models.ForeignKey(RipartizioneGeografica, on_delete=PROTECT)
    codice_istat = models.CharField(max_length=10)
    codice_catastale = models.CharField(max_length=10)
    nome = models.CharField(max_length=100, db_index=True)
    nome_de = models.CharField(max_length=100, null=True, blank=True)
    cap = models.CharField(max_length=10, null=True, blank=True)
    capoluogo = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ('nome',)
        verbose_name = "Comune"
        verbose_name_plural = "Comuni"
