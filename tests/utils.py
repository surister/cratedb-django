import dataclasses

from django.test.utils import CaptureQueriesContext


@dataclasses.dataclass
class CapturedQuery:
    _original_query: dict = dataclasses.field(repr=False)
    stmt: str = dataclasses.field(init=False)
    params: tuple = dataclasses.field(init=False)
    time: str = dataclasses.field(init=False)

    def __post_init__(self):
        _parts = self._original_query["sql"].split("-")
        self.stmt = _parts[0].split("=")[1].strip().replace("'", "")
        self.params = _parts[1].split("=")[1].strip()
        self.time = self._original_query["time"]

    def is_insert(self):
        return "insert" in self.stmt.lower()


class captured_queries(CaptureQueriesContext):
    @property
    def latest_query(self):
        return CapturedQuery(self.captured_queries[len(self.captured_queries) - 1])

    @property
    def first_query(self):
        return CapturedQuery(self.captured_queries[0])

    def query_at(self, index: int):
        """
        n is the index in an array containing all the captured queries.

        n_query(0) - is the first query, the same as `self.first_query`.
        n_query(len(queries)) - is the latest query, the same as `self.latest_query`.
        n_query(2) - is the query at index 2.
        """
        return CapturedQuery(self.captured_queries[index])
