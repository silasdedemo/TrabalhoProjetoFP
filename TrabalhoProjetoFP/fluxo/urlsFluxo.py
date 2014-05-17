from django.conf.urls import patterns, include, url

urlpatterns = patterns('fluxo.views',

    url(r'^$', 'buscaFluxo'),
)