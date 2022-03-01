# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""


class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range
        self.river = river
        self.town = town

        self.latest_level = None

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def relative_water_level(self):
        """returning latest water level as a fraction of typical range"""
    
        if self.typical_range == None: #(when no typical data is avaliable)
            return None
        elif self.typical_range[0] > self.typical_range[1]: #Returns none when data is inconsistent
            return None
        elif self.latest_level == None: #If no latest level data available, return None.
            return None
        else:
            latest_water_level_within_range = self.latest_level[0] - self.typical_range[0]
            typical_water_range = self.typical_range[1] - self.typical_range[0]
            relative_range = latest_water_level_within_range/typical_water_range
            return relative_range # returns output of 1 if at upper end of range, 0 if at low end of range. 
