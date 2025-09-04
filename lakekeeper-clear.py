from pyiceberg.catalog import load_catalog

from utils.timer import Timer
from definitions import LAKEKEEPER_CATALOG_URL, LAKEKEEPER_WAREHOUSE

timer = Timer()

lakekeeper_catalog = load_catalog(
    "default",
    type="rest",
    uri=LAKEKEEPER_CATALOG_URL,
    warehouse=LAKEKEEPER_WAREHOUSE,
)
timer.add("load_catalog")

namespaces = lakekeeper_catalog.list_namespaces()
timer.add("list_namespaces")

for namespace in namespaces:

    namespace_name, = namespace
    tables = lakekeeper_catalog.list_tables(namespace)
    timer.add(f"list_tables in namespace {namespace_name}")

    for table in tables:
        table_namespace_name, table_name = table
        lakekeeper_catalog.drop_table(table)
        timer.add(f"drop_table {table_name} in namespace {table_namespace_name}")

    lakekeeper_catalog.drop_namespace(namespace)
    timer.add(f"drop_namespace {namespace_name}")

timer.display()