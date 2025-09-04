from pyiceberg.catalog import load_catalog
from pyiceberg.table import Table
import pyarrow.parquet as pq

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

# Think of the namespace as our database schema
polaris_catalog.create_namespace_if_not_exists("webinar_namespace")
timer.add("create_namespace")

print(polaris_catalog.list_namespaces())
timer.add("list_namespaces")

df = pq.read_table("./data/yellow_tripdata_2023-01.parquet")
timer.add("read_local_parquet_table")

table_ref =polaris_catalog.create_table_if_not_exists(
    "webinar_namespace.webinar_table",
    schema=df.schema,
)
timer.add("create_table")

print(polaris_catalog.list_tables("webinar_namespace"))
timer.add("list_tables")

loaded_table_ref:Table = polaris_catalog.load_table("webinar_namespace.webinar_table")
timer.add("load_table")

# STUCK HERE
loaded_table_ref.overwrite(df)
timer.add("write_to_table")

print(len(loaded_table_ref.scan().to_arrow()))
timer.add("count_rows")

timer.display()