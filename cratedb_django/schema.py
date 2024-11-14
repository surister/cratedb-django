from django.db.backends.base.schema import BaseDatabaseSchemaEditor


class DatabaseSchemaEditor(BaseDatabaseSchemaEditor):
    # TODO DOCUMENT CAVEAT: IF YOU START WITH A DJANGO MIGRATIONS CREATED BY OTHER DATABASE LIKE POSTGRES,
    # NEW MIGRATIONS WITH NO-OP operations like drop constraint, might produce confusing behaviour, you might
    # expect things that will be no-op, like drop constraints.

    # TODO pgdiff
    # TODO, is this bug? why isn't supports_deferrable_unique_constraints respected on table creation?
    # create table contentypes to reproduce

    sql_create_unique = ('select 1')

    sql_alter_column_type = "SELECT 1"
    sql_alter_column_null = "SELECT 2"
    sql_alter_column_not_null = "SELECT 3"
    sql_alter_column_default = "SELECT 4"
    sql_alter_column_no_default = "SELECT 5"

    sql_delete_column = "ALTER TABLE %(table)s DROP COLUMN %(column)s"
    sql_delete_table = "DROP TABLE %(table)s"

    def add_index(self, model, index):
        return None

    def rename_index(self, model, old_index, new_index):
        return None

    def remove_index(self, model, index):
        return None

    def add_constraint(self, model, constraint):
        return None

    def remove_constraint(self, model, constraint):
        return None

    def _model_indexes_sql(self, model):
        """
        todo pgdiff

        This overload stops django from issuing CREATE INDEX statements.
        https://forum.djangoproject.com/t/dont-issue-create-index-on-initial-migration/36227/4
        """
        return ()

    def _alter_column_null_sql(self, model, old_field, new_field):
        return ()

    def column_sql(self, model, field, include_default=False):
        field.unique = False
        # todo pgdiff
        return super().column_sql(model=model, field=field, include_default=include_default)