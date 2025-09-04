from pyiceberg.catalog import load_catalog
from pyiceberg.table import Table
import pyarrow.parquet as pq

from utils.timer import Timer
from definitions import (
    LAKEKEEPER_CATALOG_URL,
    LAKEKEEPER_WAREHOUSE,
)

timer = Timer()

lakekeeper_catalog = load_catalog(
    "default",
    type="rest",
    uri=LAKEKEEPER_CATALOG_URL,
    warehouse=LAKEKEEPER_WAREHOUSE, # Think of the warehouse as our database
)
timer.add("load_catalog")

# Think of the namespace as our database schema
lakekeeper_catalog.create_namespace_if_not_exists("webinar_namespace")
timer.add("create_namespace")

print(lakekeeper_catalog.list_namespaces())
timer.add("list_namespaces")

df = pq.read_table("./data/yellow_tripdata_2023-01.parquet")
timer.add("read_local_parquet_table")

table_ref =lakekeeper_catalog.create_table_if_not_exists(
    "webinar_namespace.webinar_table",
    schema=df.schema,
)
timer.add("create_table")

print(lakekeeper_catalog.list_tables("webinar_namespace"))
timer.add("list_tables")

loaded_table_ref:Table = lakekeeper_catalog.load_table("webinar_namespace.webinar_table")
timer.add("load_table")

# STUCK HERE
loaded_table_ref.overwrite(df)
timer.add("write_to_table")

print(len(loaded_table_ref.scan().to_arrow()))
timer.add("count_rows")

timer.display()