import pycountry

from django.core.management.base import BaseCommand, CommandError

from country_search.elastic_connection import SearchEngineConnection

es = SearchEngineConnection().connection


class Command(BaseCommand):
    help = 'Populates elasticsearch search engine with data if required.'

    def handle(self, *args, **options):
        if es.indices.exists(index=SearchEngineConnection.countries_index):
            print("Countries index exists, nothing to do here.")
            return
        print("Countries index doesn't exist, creating . . .")
        # TODO: Bulk create
        # TODO: Move this to connection.py
        es.indices.delete(index=SearchEngineConnection.countries_index,
                          ignore=[400, 404])
        es.indices.create(index=SearchEngineConnection.countries_index)
        # generate "country" data for search engine
        for idx, country in enumerate(pycountry.countries):
            country_body = SearchEngineConnection.get_country_body(
                country.name, country.alpha_2, country.alpha_3)

            res = es.index(index=SearchEngineConnection.countries_index,
                           doc_type=SearchEngineConnection.country_doc,
                           id=idx, body=country_body)
        # refresh search engine so that data is available
        es.indices.refresh(index=SearchEngineConnection.countries_index)
        print("Search engine data populated")
