from django.shortcuts import render
from django.http import HttpResponse

from .elastic_connection import SearchEngineConnection

connection = SearchEngineConnection()


def index(request):
    # TODO: Implement country search
    countries = connection.search_all_countries()
    context = {"countries": countries}
    return render(request, 'country_search/index.html', context)
