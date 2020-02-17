import logging
import numpy as np

from enum import Enum
from netCDF4 import Dataset, Group
from typing import Optional

from hyo2.openbst.lib.nc_helper import NetCDFHelper

logger = logging.getLogger(__name__)


# ## Sounding Position Enum and Dictionaries ##
class GeolocateEnum(Enum):
    compute = 0
    imported_bathy = 1


geolocate_title = {
    GeolocateEnum.compute: "Sounding Position - Computed",
    GeolocateEnum.imported_bathy: "Sounding Position - Imported"
}


# ## Positioning Parameters Object ##
class GeolocationParams:
    process_name = "sounding_positioning"

    def __init__(self):
        self.method_type = GeolocateEnum.slant_range
        self.motion_comp = False
        self.raytrace = False

    def nc_write_parameters(self, grp_process: Group):
        try:
            grp_process.title = geolocate_title[self.method_type]
            grp_process.method_type = self.method_type.name
            grp_process.motion_comp = str(self.motion_comp)
            grp_process.raytrace = str(self.raytrace)
            return True

        except TypeError:
            return False

    def process_identifiers(self) -> list:
        process_string = GeolocationParams.process_name
        parameter_string = str()
        for key, value in self.__dict__.items():
            parameter_string += key + str(value)
        parameter_hash = NetCDFHelper.hash_string(input_str=parameter_string)
        process_ids = [process_string, parameter_hash]
        return process_ids


# ## Positioning Class and methods ##
class Geolocation:

    def __init__(self):
        pass

    @classmethod
    def position_soundings(cls, ds_process: Dataset, ds_raw: Dataset,
                           parent: str, parameters: GeolocationParams):
        p_method_type = parameters.method_type
        p_motion_comp = parameters.motion_comp

        if p_method_type is GeolocateEnum.compute:
            data_out = Geolocation.slant_range()

        elif p_method_type is GeolocateEnum.imported_bathy:
            data_out = Geolocation.import_bathy()
        else:
            raise TypeError("Unrecognized Geolocation Method: %s" % p_method_type)
        return data_out

    @classmethod
    def write_data_to_nc(cls):
        pass

    # # Processing Methods Types:
    @classmethod
    def compute(cls,
                sample_rate: np.ma.MaskedArray,
                sensor_sound_speed: Optional[np.ma.MaskedArray],
                detection_point: np.ma.MaskedArray,
                lat: np.ma.MaskedArray,
                lon: np.ma.MaskedArray,
                roll: Optional[np.ma.MaskedArray],
                pitch: Optional[np.ma.MaskedArray],
                yaw: Optional[np.ma.MaskedArray]):

        # Calculate the range
        if sensor_sound_speed is None:
                sensor_sound_speed = 1500   # A static value of 1500m/s


        range_m = detection_point / sample_rate * sensor_sound_speed / 2




    @classmethod
    def import_bathy(cls):
        pass
