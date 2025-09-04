from pyiceberg.catalog import load_catalog
from pyiceberg.table import Table
import pyarrow.parquet as pq

from utils.timer import Timer
from definitions import (
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    AWS_REGION,
    S3_BUCKET_NAME,
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

# Think of the namespace as our database schema
glue_catalog.create_namespace_if_not_exists("webinar_namespace")
timer.add("create_namespace")

print(glue_catalog.list_namespaces())
timer.add("list_namespaces")

df = pq.read_table("./data/yellow_tripdata_2023-01.parquet")
timer.add("read_local_parquet_table")

table_ref =glue_catalog.create_table_if_not_exists(
    "webinar_namespace.webinar_table",
    schema=df.schema,
    location=f"s3://{S3_BUCKET_NAME}/glue/webinar_namespace/webinar_table",
)
timer.add("create_table")

print(glue_catalog.list_tables("webinar_namespace"))
timer.add("list_tables")

loaded_table_ref:Table = glue_catalog.load_table("webinar_namespace.webinar_table")
timer.add("load_table")

# STUCK HERE
loaded_table_ref.overwrite(df)
timer.add("write_to_table")

print(len(loaded_table_ref.scan().to_arrow()))
timer.add("count_rows")

timer.display()