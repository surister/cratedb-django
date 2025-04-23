import datetime

from django.forms.models import model_to_dict

try:
    from example.apps.simple_auth.models import MigrationTest
except:
    from apps.simple_auth.models import MigrationTest

from tests import NoTransactionTestCase


class MigrationTestTests(NoTransactionTestCase):
    def tearDown(self):
        # Clean up after each test
        MigrationTest.objects.all().delete()
        MigrationTest.refresh()
        # pass

    def test_simple_create(self):
        """Test that an object is created and accounted for with all fields"""
        assert MigrationTest.objects.count() == 0
        expected = {
            "id": 29147646,
            "field_int": 1,
            "field_int_unique": 2,
            "field_int_not_indexed": 3,
            "field_int_not_null": 4,
            "field_int_null": 5,
            "field_int_default": 6,
            "field_float": 0.1,
            "field_char": "somechar",
            "field_bool": True,
            "field_date": datetime.datetime(2025, 4, 23, 0, 0),
            "field_datetime": datetime.datetime(2025, 4, 23, 14, 20, 15, 833000),
            "field_json": {"hello": "world"},
            "field_uuid": "00bde3702f844402b750c1b37d589084",
        }
        MigrationTest.objects.create(**expected)
        MigrationTest.refresh()
        assert MigrationTest.objects.count() == 1

        obj = MigrationTest.objects.get()
        assert model_to_dict(obj) == expected

    def test_unique_duplicates(self):
        # CrateDB does not support the unique constraint, creating two test objects which
        # has static values should not error.
        MigrationTest.create_test()
        MigrationTest.create_test()
        MigrationTest.refresh()
        assert MigrationTest.objects.count() == 2

    def test_random_id(self):
        MigrationTest.create_test()
        MigrationTest.refresh()
        obj = MigrationTest.objects.get()
        assert hasattr(obj, 'id')
        assert isinstance(obj.id, int)
