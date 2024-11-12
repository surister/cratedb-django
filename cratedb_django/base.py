from crate.client.converter import DefaultTypeConverter
from crate.client.cursor import Cursor
from crate.client.connection import Connection
from django.core.exceptions import ImproperlyConfigured

from django.db.backends.base.base import BaseDatabaseWrapper

from .client import DatabaseClient
from .creation import DatabaseCreation
from .features import DatabaseFeatures
from .introspection import DatabaseIntrospection
from .operations import DatabaseOperations
from .schema import DatabaseSchemaEditor


def _get_varchar_column(data):
    if data["max_length"] is None:
        return "varchar"
    return "varchar(%(max_length)s)" % data


class DatabaseWrapper(BaseDatabaseWrapper):
    vendor = 'Crate.io'
    display_name = 'CrateDB'

    client_class = DatabaseClient
    creation_class = DatabaseCreation
    features_class = DatabaseFeatures
    introspection_class = DatabaseIntrospection
    ops_class = DatabaseOperations
    SchemaEditorClass = DatabaseSchemaEditor

    CRATE_SQL_SERIAL = 'TEXT GENERATED ALWAYS AS gen_random_text_uuid()'
    data_types = {
        # todo pgdiff - doc
        "AutoField": CRATE_SQL_SERIAL,
        "BigAutoField": CRATE_SQL_SERIAL,
        "SmallAutoField": CRATE_SQL_SERIAL,

        "BinaryField": "bytea",
        "BooleanField": "boolean",
        "CharField": _get_varchar_column,
        "DateField": "date",
        "DateTimeField": "timestamp with time zone",
        "DecimalField": "numeric(%(max_digits)s, %(decimal_places)s)",
        "DurationField": "interval",
        "FileField": "varchar(%(max_length)s)",
        "FilePathField": "varchar(%(max_length)s)",
        "FloatField": "double precision",
        "IntegerField": "integer",
        "BigIntegerField": "bigint",
        "IPAddressField": "IP",
        "GenericIPAddressField": "inet",
        "JSONField": "jsonb",
        "OneToOneField": "integer",
        "PositiveBigIntegerField": "bigint",
        "PositiveIntegerField": "integer",
        "PositiveSmallIntegerField": "smallint",
        "SlugField": "varchar(%(max_length)s)",

        "SmallIntegerField": "smallint",
        "TextField": "text",
        "TimeField": "time",
        "UUIDField": "uuid",
    }

    def _set_autocommit(self, autocommit):
        with self.wrap_database_errors:
            self.connection.autocommit = autocommit

    def get_connection_params(self):
        conn_params = dict(servers=self.settings_dict.get('SERVERS'))

        if self.settings_dict["HOST"]:
            conn_params["servers"] = [self.settings_dict["HOST"]]

        if self.settings_dict.get("PORT") or self.settings_dict.get("HOST"):
            raise ImproperlyConfigured(
                "Do not use 'PORT' nor 'HOST' in settings.databases, user 'SERVERS'"
            )

        return conn_params

    def get_new_connection(self, conn_params):
        return Connection(**conn_params)

    def create_cursor(self, name=None):
        return Cursor(self.connection, DefaultTypeConverter())
