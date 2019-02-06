from elasticsearch import Elasticsearch, RequestsHttpConnection

from django.conf import settings


class SearchEngineConnection(object):
    """Singleton pattern to ensure only on elasticsearch connection is made."""
    _es = None
    countries_index = "countries"
    country_doc = "country"

    def __init__(self):
        self.es = self.get_es_connection()

    @classmethod
    def get_es_connection(cls):
        if SearchEngineConnection._es is None:
            SearchEngineConnection._es = Elasticsearch(
                settings.ELASTICSEARCH_HOST,
                connection_class=RequestsHttpConnection)
        return SearchEngineConnection._es

    @staticmethod
    def get_country_body(country_name, iso_2, iso_3):
        return {
            "name": country_name,
            "iso_2": iso_2,
            "iso_3": iso_3,
        }

    def get_hits(self, res):
        return [country["_source"] for country in res["hits"]["hits"]]

    def search_all_countries(self):
        query = {
            "from": 0,
            "size": 400,
            "query": {
                "match_all": {}
            }
        }
        res = self.es.search(
            index=self.countries_index,
            body=query,
        )
        return self.get_hits(res)

    def basic_country_search(self, search_term):
        query = {
            "query": {
                "match": {
                    "name": {
                        "query": search_term,
                        "fuzziness": "AUTO",
                    }
                }
            }
        }
        res = self.es.search(index=self.countries_index, body=query)
        return self.get_hits(res)
