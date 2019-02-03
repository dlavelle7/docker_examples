from django.core.management.base import BaseCommand, CommandError

from country_search.elastic_connection import SearchEngineConnection


class Command(BaseCommand):
    help = 'Populates elasticsearch search engine with data if required.'

    def handle(self, *args, **options):
        print('hi')
