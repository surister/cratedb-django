import uuid
from datetime import datetime

from django.db import models

from cratedb_django import CrateModel
from cratedb_django.models import ObjectField


class MigrationTest(CrateModel):
    field_int = models.IntegerField(unique=False)
    field_int_unique = models.IntegerField(unique=True)
    field_int_not_indexed = models.IntegerField(db_index=False)
    field_int_not_null = models.IntegerField(null=False)
    field_int_null = models.IntegerField(null=True)
    field_int_default = models.IntegerField(default=54321)
    field_float = models.FloatField()
    field_char = models.CharField(max_length=100)
    field_bool = models.BooleanField()
    field_date = models.DateField()
    field_datetime = models.DateTimeField()
    field_json = ObjectField(default=dict)
    field_uuid = models.UUIDField()

    @classmethod
    def create_test(cls):
        return cls.objects.create(
            field_int=1,
            field_int_unique=2,
            field_int_not_indexed=3,
            field_int_not_null=4,
            field_int_null=5,
            field_int_default=6,
            field_float=0.1,
            field_char="somechar",
            field_bool=True,
            field_date=datetime.today().date(),
            field_datetime=datetime.today(),
            field_json={"hello": "world"},
            field_uuid=uuid.uuid4(),
        )

    class Meta:
        pass
        # unique_together = (('field_int', 'field_char'),)
        # indexes = [
        #     models.Index(fields=['field_bool']),
        #     models.Index(fields=['field_date']),
        # ]
