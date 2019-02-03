from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from elasticsearch import Elasticsearch, RequestsHttpConnection


# TODO: Management command to load data
# TODO: Put in own module so it can be reused
class SearchEngineConnection(object):
    """Singleton pattern to ensure only on elasticsearch connection is made."""
    _connection = None
    host = "elastic"  # host name of docker container

    def __init__(self):
        self.connection = self.get_connection()

    @classmethod
    def get_connection(cls):
        if SearchEngineConnection._connection is None:
            SearchEngineConnection._connection = Elasticsearch(
                settings.ELASTICSEARCH_HOST,
                connection_class=RequestsHttpConnection)
        return SearchEngineConnection._connection


def index(request):
    es = SearchEngineConnection().connection
    res = es.search(index="countries", body={"query": {"match_all": {}}})
    context = {"countries": res}
    return render(request, 'country_search/index.html', context)
