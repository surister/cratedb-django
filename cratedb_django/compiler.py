from django.db.models.sql.compiler import (
    SQLCompiler,
)  # noqa -- Import needed for re-imports.

from django.db.models.sql.compiler import (
    SQLInsertCompiler,
    SQLUpdateCompiler,
    SQLAggregateCompiler,
    SQLDeleteCompiler,
    SQLCompiler,
)


class SQLInsertCompiler(SQLInsertCompiler):
    pass


class SQLDeleteCompiler(SQLDeleteCompiler):
    pass


class SQLUpdateCompiler(SQLUpdateCompiler):
    pass


class SQLAggregateCompiler(SQLAggregateCompiler):
    pass
