from pyiceberg.catalog import load_catalog

from utils.timer import Timer
from definitions import (
    POLARIS_CATALOG_URL,
    POLARIS_WAREHOUSE,
    POLARIS_USER_CLIENT_ID,
    POLARIS_USER_CLIENT_SECRET,
)

timer = Timer()

polaris_catalog = load_catalog(
    "default",
    type="rest",
    uri=POLARIS_CATALOG_URL,
    warehouse=POLARIS_WAREHOUSE, # Think of the warehouse as our workspace
    scope="PRINCIPAL_ROLE:ALL",
    credential=f"{POLARIS_USER_CLIENT_ID}:{POLARIS_USER_CLIENT_SECRET}",
)
timer.add("load_catalog")

namespaces = polaris_catalog.list_namespaces()
timer.add("list_namespaces")

for namespace in namespaces:

    namespace_name, = namespace
    tables = polaris_catalog.list_tables(namespace)
    timer.add(f"list_tables in namespace {namespace_name}")

    for table in tables:
        table_namespace_name, table_name = table
        polaris_catalog.drop_table(table)
        timer.add(f"drop_table {table_name} in namespace {table_namespace_name}")

    polaris_catalog.drop_namespace(namespace)
    timer.add(f"drop_namespace {namespace_name}")

timer.display()