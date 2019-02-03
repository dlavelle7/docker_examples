from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {}
    return render(request, 'country_search/index.html', context)
