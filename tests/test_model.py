from django.forms.models import model_to_dict
from tests.test_app.models import AllFieldsModel, SimpleModel, RefreshModel
from django.db import connection
from django.test.utils import CaptureQueriesContext

def test_refresh():
    """Test that Model.refresh() works"""
    with CaptureQueriesContext(connection) as ctx:
        RefreshModel.refresh()
        assert 'refresh table test_app_refreshmodel' in ctx.captured_queries[0]['sql']

def test_insert_model_field():
    """Test that we can insert a model and refresh it"""
    assert SimpleModel.objects.count() == 0
    SimpleModel.objects.create(field="text")
    SimpleModel.refresh()
    assert SimpleModel.objects.count() == 1


def test_insert_all_fields():
    """Test that an object is created and accounted for with all fields"""

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
        # "field_date": datetime.datetime(2025, 4, 22, 0, 0, tzinfo=datetime.timezone.utc),
        # "field_datetime": datetime.datetime(1, 1, 1, 1, 1, 1, 1),
        "field_json": {"hello": "world"},
        "field_uuid": "00bde3702f844402b750c1b37d589084",
    }
    AllFieldsModel.objects.create(**expected)
    AllFieldsModel.refresh()
    assert AllFieldsModel.objects.count() == 1

    obj = AllFieldsModel.objects.get()
    assert model_to_dict(obj) == expected
