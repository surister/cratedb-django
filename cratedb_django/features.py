from django.db.backends.base.features import BaseDatabaseFeatures


class DatabaseFeatures(BaseDatabaseFeatures):
    # Does the backend support partial indexes (CREATE INDEX ... WHERE ...)?
    supports_partial_indexes = False
    supports_functions_in_partial_indexes = False

    # Does the backend support indexes on expressions?
    supports_expression_indexes = False

    supports_foreign_keys = False
    supports_comments = False

    can_rollback_ddl = False

    def supports_transactions(self):
        return False
