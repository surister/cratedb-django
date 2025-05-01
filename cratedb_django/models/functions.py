from django.db.models.expressions import Func

"""
class SomeTestModel(CrateModel):
    id = models.TextField(primary_key=True, db_default=UUID())
    some = models.TextField()
"""

class UUID(Func):
    """https://cratedb.com/docs/crate/reference/en/latest/general/builtins/scalar-functions.html#gen-random-text-uuid"""
    function = "gen_random_text_uuid"
