from django.db.backends.base.base import BaseDatabaseWrapper


class DatabaseWrapper(BaseDatabaseWrapper):
    vendor = 'Crate.io'
    display_name = 'CrateDB'
