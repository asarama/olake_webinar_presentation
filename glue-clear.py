from pyiceberg.catalog import load_catalog

from utils.timer import Timer
from definitions import (
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    AWS_REGION,
)

timer = Timer()

glue_catalog = load_catalog(
    'default',
    **{
        'client.access-key-id': AWS_ACCESS_KEY_ID,
        'client.secret-access-key': AWS_SECRET_ACCESS_KEY,
        'client.region': AWS_REGION,
    },
    type='glue'
)
timer.add("load_catalog")

namespaces = glue_catalog.list_namespaces()
timer.add("list_namespaces")

for namespace in namespaces:

    namespace_name, = namespace
    tables = glue_catalog.list_tables(namespace)
    timer.add(f"list_tables in namespace {namespace_name}")

    for table in tables:
        table_namespace_name, table_name = table
        glue_catalog.drop_table(table)
        timer.add(f"drop_table {table_name} in namespace {table_namespace_name}")

    glue_catalog.drop_namespace(namespace)
    timer.add(f"drop_namespace {namespace_name}")

timer.display()