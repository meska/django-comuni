from django.contrib import admin

from comuni.models import Regione, Comune, Provincia, RipartizioneGeografica


class ComuneAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'nome_de',
        'provincia',
        'ripartizione',
        'codice_istat',
        'codice_catastale',
        'cap',
        'capoluogo'
    )
    list_filter = ('provincia', 'ripartizione',)
    search_fields = ('nome', 'codice_istat', 'cap')


class ProvinciaAdmin(admin.ModelAdmin):
    list_display = (
        'nome',
        'nome_de',
        'codice',
        'sigla',
        'regione',
    )
    list_filter = ('regione',)
    search_fields = ('nome', 'sigla')


class RipartizioneGeograficaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codice')
    search_fields = ('nome',)


class RegioneAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nome_de', 'codice')
    search_fields = ('nome',)


admin.site.register(Comune, ComuneAdmin)
admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(RipartizioneGeografica, RipartizioneGeograficaAdmin)
admin.site.register(Regione, RegioneAdmin)
