from django.shortcuts import render
from django.http import HttpResponse

from .elastic_connection import SearchEngineConnection

es = SearchEngineConnection().connection


def index(request):
    res = es.search(index=SearchEngineConnection.countries_index,
                    body={"query": {"match_all": {}}})
    context = {"countries": res}
    return render(request, 'country_search/index.html', context)
