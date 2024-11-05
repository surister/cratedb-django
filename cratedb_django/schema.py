from django.db.backends.base.schema import BaseDatabaseSchemaEditor


class DatabaseSchemaEditor(BaseDatabaseSchemaEditor):
    def column_sql(self, model, field, include_default=False):
        t = super().column_sql(model, field, include_default)
        return t