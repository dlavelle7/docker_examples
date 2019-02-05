from django.shortcuts import render
from django.http import HttpResponse

from .elastic_connection import SearchEngineConnection

connection = SearchEngineConnection()


def index(request):
    # TODO: Have "show all countries" option
    # TODO: Have GET by ID option
    search_term = request.GET.get("search")
    context = {}
    if search_term is not None:
        context["countries"] = connection.basic_country_search(search_term)
        context["headers"] = ["Country Name", "ISO 3 Code", "ISO 2 Code"]
    return render(request, 'country_search/index.html', context)
