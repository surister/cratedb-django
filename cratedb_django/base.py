from crate.client.converter import DefaultTypeConverter
from crate.client.cursor import Cursor
from crate.client.connection import Connection

from django.db.backends.base.base import BaseDatabaseWrapper

from .client import DatabaseClient
from .creation import DatabaseCreation
from .features import DatabaseFeatures
from .introspection import DatabaseIntrospection
from .operations import DatabaseOperations


class DatabaseWrapper(BaseDatabaseWrapper):
    vendor = 'Crate.io'
    display_name = 'CrateDB'

    client_class = DatabaseClient
    creation_class = DatabaseCreation
    features_class = DatabaseFeatures
    introspection_class = DatabaseIntrospection
    ops_class = DatabaseOperations

    def _set_autocommit(self, autocommit):
        with self.wrap_database_errors:
            self.connection.autocommit = autocommit

    def get_connection_params(self):
        return {
            "servers": ["localhost:4200"]
        }

    def get_new_connection(self, conn_params):
        return Connection(**conn_params)

    def create_cursor(self, name=None):
        return Cursor(self.connection, DefaultTypeConverter())
