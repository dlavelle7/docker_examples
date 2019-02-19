import pycountry

from django.core.management.base import BaseCommand

from country_search.elastic_connection import SearchEngineConnection

conn = SearchEngineConnection()


class Command(BaseCommand):
    help = 'Populates elasticsearch search engine with data if required.'

    def handle(self, *args, **options):
        if conn.es.indices.exists(index=conn.countries_index):
            print("Countries index exists, nothing to do here.")
            return
        print("Countries index doesn't exist, creating . . .")
        # TODO: Never refer to index by name, use an alias
        # TODO: Bulk create
        conn.es.indices.delete(index=conn.countries_index, ignore=[400, 404])
        conn.es.indices.create(index=conn.countries_index)
        # generate "country" data for search engine
        for idx, country in enumerate(pycountry.countries):
            country_body = conn.get_country_body(
                country.name, country.alpha_2, country.alpha_3)
            conn.es.index(
                index=conn.countries_index, doc_type=conn.country_doc,
                id=idx, body=country_body)
        # refresh search engine so that data is available
        conn.es.indices.refresh(index=conn.countries_index)
        print("Search engine data populated")
