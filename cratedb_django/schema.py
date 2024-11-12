from django.db.backends.base.schema import BaseDatabaseSchemaEditor


class DatabaseSchemaEditor(BaseDatabaseSchemaEditor):
    sql_create_index = "SELECT 1"

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
