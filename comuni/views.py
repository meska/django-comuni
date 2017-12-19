from django.http import JsonResponse
from django.views import View

from comuni.models import Comune


class ComuneAutoComplete(View):
    """
    Json Response for select2 input
    """

    # noinspection PyMethodMayBeStatic
    def get(self, request):
        q = request.GET.get('q')
        if q:
            comuni = Comune.objects.filter(nome__icontains=q).select_related('provincia')
        else:
            comuni = Comune.objects.all().select_related('provincia')[0:10]

        return JsonResponse([dict(id=c.pk, text=f"{c.nome} ({c.provincia.sigla})") for c in comuni], safe=False)


class ComuneJson(View):

    # noinspection PyMethodMayBeStatic,PyUnusedLocal
    def get(self, request, nome):
        if nome.isdigit():
            comune = Comune.objects.filter(pk=nome).first()
        else:
            comune = Comune.objects.filter(nome=nome).first()
        if comune:
            return JsonResponse(
                dict(
                    id=comune.pk,
                    text=comune.nome,
                    cap=comune.cap,
                    provincia=comune.provincia.sigla,
                    regione=comune.provincia.regione.nome,
                    zona=comune.ripartizione.nome
                )
            )
        else:
            return JsonResponse(dict(id=nome, text=nome))
