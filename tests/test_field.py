from django.db import connection, models
from cratedb_django.models import functions

def test_field_with_uuid_default():
    """
    Tests a Model field with a db_default of UUID
    """

    class TestModel(models.Model):
        f = models.TextField(db_default=functions.UUID())

        class Meta:
            app_label = 'ignore'

    with connection.schema_editor() as schema_editor:
        sql, params = schema_editor.column_sql(TestModel, TestModel._meta.get_field('f'))
        assert sql == 'text DEFAULT (gen_random_text_uuid()) NOT NULL'
