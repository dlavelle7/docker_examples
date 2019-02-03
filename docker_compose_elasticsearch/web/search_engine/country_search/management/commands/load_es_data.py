from django.core.management.base import BaseCommand, CommandError

from country_search.elastic_connection import SearchEngineConnection

es = SearchEngineConnection().connection


class Command(BaseCommand):
    help = 'Populates elasticsearch search engine with data if required.'

    def handle(self, *args, **options):
        if es.indices.exists(index=SearchEngineConnection.countries_index):
            print("Countries index exists, nothing to do here.")
        else:
            print("Countries index doesn't exist, creating . . .")
