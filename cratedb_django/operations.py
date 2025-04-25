from django.db.backends.base.operations import BaseDatabaseOperations


class DatabaseOperations(BaseDatabaseOperations):
    compiler_module = "cratedb_django.compiler"

    def quote_name(self, name) -> str:
        if name.startswith('"') and name.endswith('"'):
            return name  # Quoting once is enough.
        return f'"{name}"'

    def sql_flush(self, style, tables, *, reset_sequences=False, allow_cascade=False) -> list[str]:
        return [f"DELETE FROM {table}" for table in tables]
