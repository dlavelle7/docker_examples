from elasticsearch import Elasticsearch, RequestsHttpConnection

from django.conf import settings


class SearchEngineConnection(object):
    """Singleton pattern to ensure only on elasticsearch connection is made."""
    _connection = None
    countries_index = "countries"

    def __init__(self):
        self.connection = self.get_connection()

    @classmethod
    def get_connection(cls):
        if SearchEngineConnection._connection is None:
            SearchEngineConnection._connection = Elasticsearch(
                settings.ELASTICSEARCH_HOST,
                connection_class=RequestsHttpConnection)
        return SearchEngineConnection._connection
