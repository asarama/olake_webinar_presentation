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

lakekeeper_catalog.drop_namespace("hello_world")
timer.add("drop_namespace")


lakekeeper_catalog.drop_namespace("hello_world_2")
timer.add("drop_namespace_2")

timer.display()