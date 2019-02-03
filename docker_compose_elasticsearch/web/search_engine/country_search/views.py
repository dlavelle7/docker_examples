from django.shortcuts import render
from django.http import HttpResponse

from .elastic_connection import SearchEngineConnection

connection = SearchEngineConnection()


def index(request):
    # TODO: Implement actual country search
    search_term = request.GET.get("search")
    context = {}
    if search_term is not None:
        context["countries"] = connection.search_all_countries()
        context["headers"] = ["Country Name", "ISO 3 Code", "ISO 2 Code"]
    return render(request, 'country_search/index.html', context)
