from pyiceberg.catalog import load_catalog

from utils.timer import Timer

timer = Timer()

timer.add("init")
lakekeeper_catalog = load_catalog(
    "default",
    type="rest",
    uri="http://0.0.0.0:8181/catalog/",
    warehouse="webinar",
)
timer.add("load_catalog")

lakekeeper_catalog.create_namespace_if_not_exists("hello_world")
timer.add("create_namespace")


lakekeeper_catalog.create_namespace_if_not_exists("hello_world_2")
timer.add("create_namespace_2")

timer.display()