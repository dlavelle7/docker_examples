from django.shortcuts import render
from django.http import HttpResponse

from .elastic_connection import SearchEngineConnection

connection = SearchEngineConnection()


def index(request):
    # TODO: Implement country search
    search_term = request.GET.get("search")
    if search_term is not None:
        countries = connection.search_all_countries()
    else:
        countries = None
    context = {"countries": countries}
    return render(request, 'country_search/index.html', context)
