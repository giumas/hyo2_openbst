import logging
import numpy as np

from enum import Enum
from netCDF4 import Dataset, Group

from hyo2.openbst.lib.nc_helper import NetCDFHelper

logger = logging.getLogger(__name__)


# ## Sounding Position Enum and Dictionaries ##
class GeolocateEnum(Enum):
    slant_range = 0
    raytrace = 1
    imported_bathy = 2


position_title = {
    GeolocateEnum.slant_range: "Sounding Position - Slant Range Approximation",
    GeolocateEnum.raytrace: "Sounding Position - Raytraced",
    GeolocateEnum.imported_bathy: "Sounding Position - Imported"
}


# ## Positioning Parameters Object ##
class GeolocationParams:
    process_name = "sounding_positioning"

    def __init__(self):
        self.method_type = GeolocateEnum.slant_range
        self.motion_comp = False

    def nc_write_parameters(self, grp_process: Group):
        pass

    def process_identifiers(self) -> list:
        pass


# ## Positioning Class and methods ##
class Geolocation:

    def __init__(self):
        pass

    @classmethod
    def position_soundings(cls, ds_process: Dataset, ds_raw: Dataset,
                           parent: str, parameters: GeolocationParams):
        pass

    @classmethod
    def write_data_to_nc(cls):
        pass

    # # Processing Methods Types:
    @classmethod
    def slant_range(cls):
        pass

    @classmethod
    def raytrace(cls):
        pass

    @classmethod
    def import_bathy(cls):
        pass
