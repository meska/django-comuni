from django.conf.urls import url

from comuni.views import ComuneAutoComplete, ComuneJson

app_name = 'comuni'

urlpatterns = [
    url(r'^autocomplete/$', ComuneAutoComplete.as_view(), name='autocomplete'),
    url(r'^(?P<nome>.*)/$', ComuneJson.as_view(), name='comune'),
]
