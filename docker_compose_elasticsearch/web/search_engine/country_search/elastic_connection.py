from elasticsearch import Elasticsearch, RequestsHttpConnection


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
