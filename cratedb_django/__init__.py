from django.db import models, connection


class CrateModel(models.Model):
    """
    A base class for Django models with extra CrateDB specific functionality,

    Methods:
        refresh: Refreshes the given model (table)
    """
    @classmethod
    def refresh(cls):
        with connection.cursor() as cursor:
            cursor.execute(f"refresh table {cls._meta.db_table}")

    class Meta:
        abstract = True