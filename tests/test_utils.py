from django.db import connection

from tests.utils import captured_queries


def test_captured_queries():
    with captured_queries(connection) as ctx:
        connection.cursor().execute('select 1')
        connection.cursor().execute('select 2')
        connection.cursor().execute('select 3')

        assert ctx.first_query.stmt == 'select 1'
        assert ctx.query_at(1).stmt == 'select 2'
        assert ctx.latest_query.stmt == 'select 3'
