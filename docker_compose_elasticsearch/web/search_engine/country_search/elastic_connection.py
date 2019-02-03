from elasticsearch import Elasticsearch, RequestsHttpConnection

from django.conf import settings


class SearchEngineConnection(object):
    """Singleton pattern to ensure only on elasticsearch connection is made."""
    _connection = None
    countries_index = "countries"
    country_doc = "country"

    def __init__(self):
        self.connection = self.get_connection()

    @classmethod
    def get_connection(cls):
        if SearchEngineConnection._connection is None:
            SearchEngineConnection._connection = Elasticsearch(
                settings.ELASTICSEARCH_HOST,
                connection_class=RequestsHttpConnection)
        return SearchEngineConnection._connection

    @staticmethod
    def get_country_body(country_name, iso_2, iso_3):
        return {
            "name": country_name,
            "iso_2": iso_2,
            "iso_3": iso_3,
        }

    def search_all_countries(self):
        res = self.connection.search(index=self.countries_index,
                                     body={"query": {"match_all": {}}})
        return [country["_source"] for country in res["hits"]["hits"]]
