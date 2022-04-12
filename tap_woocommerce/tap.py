"""woocommerce tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers
# TODO: Import your custom stream types here:
from tap_woocommerce.streams import (
    woocommerceStream,
     BrandsStream, ProductsStream
)
# TODO: Compile a list of custom stream types here
#       OR rewrite discover_streams() below with your custom logic.
STREAM_TYPES = [
    BrandsStream,ProductsStream

]


class Tapwoocommerce(Tap):
    """woocommerce tap class."""
    name = "tap-woocommerce"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property(
            "username",
            th.StringType,
            required=True,
            description="Woocommerce key"
        ),
        th.Property(
            "password",
            th.StringType,
            required=True,
            description="Woo commerce secret key"
        ),
        #th.Property(
        #    "start_date",
        #    th.DateTimeType,
         #   description="The earliest record date to sync"
        #),
        th.Property(
            "api_url",
            th.StringType,
            default="https://soma.no/wp-json/wc/v3",
            description="The url for the API service"
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
