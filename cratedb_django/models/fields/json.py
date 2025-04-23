from django.db import models


class ObjectField(models.JSONField):
    def from_db_value(self, value, expression, connection):
        return value

    def get_internal_type(self):
        return "ObjectField"
