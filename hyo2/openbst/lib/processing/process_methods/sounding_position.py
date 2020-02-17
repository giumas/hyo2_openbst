import logging
import numpy as np

from enum import Enum
from netCDF4 import Dataset, Group

from hyo2.openbst.lib.nc_helper import NetCDFHelper

logger = logging.getLogger(__name__)


# ## Sounding Position Enum and Dictionaries ##
class PositioningEnum(Enum):
    slant_range = 0
    raytrace = 1
    imported_bathy = 2


position_title = {
    PositioningEnum.slant_range: "Sounding Position - Slant Range Approximation",
    PositioningEnum.raytrace: "Sounding Position - Raytraced"
    PositioningEnum.imported_bathy: "Sounding Position - Imported"
}


# ## Positioning Parameters Object ##
class PositioningParameters:
    process_name = "sounding_positioning"

    def __init__(self):
        self.method_type = PositioningEnum.slant_range
        self.motion_comp = False

    def nc_write_parameters(self,grp_process: Group):
        pass

    def process_identifiers(self) -> list:
        pass


# ## Positioning Class and methods ##
class Positioning:

    def __init__(self):
        pass

    @classmethod
    def position_soundings(cls):
        pass

    @classmethod
    def write_data_to_nc(cls):
        pass

    # # Processing Methods Types:
    @classmethod
    def slant_range(cls):
        pass

    def raytrace(self):
        pass
