from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from .elastic_connection import SearchEngineConnection


def index(request):
    es = SearchEngineConnection().connection
    res = es.search(index="countries", body={"query": {"match_all": {}}})
    context = {"countries": res}
    return render(request, 'country_search/index.html', context)
