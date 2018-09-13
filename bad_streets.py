import requests
import json
import operator

class Accident:

    def __init__(self, data):
        
        self.file_number                = str(data['file_number'])          if 'file_number' in data else None
        self.crash_date                 = str(data['crash_date'])           if 'crash_date' in data else None
        self.crash_time                 = str(data['crash_time'])           if 'crash_time' in data else None
        self.total_vehicles_involved    = str(data['tot_veh'])              if 'tot_veh' in data else None
        self.district                   = str(data['district'])             if 'district' in data else None
        self.zone                       = str(data['zone'])                 if 'zone' in data else None
        self.sub_zone                   = str(data['subzone'])              if 'subzone' in data else None
        self.street_number              = str(data['st_number'])            if 'st_number' in data else None
        self.street_direction           = str(data['st_direction'])         if 'st_direction' in data else None
        self.street_name                = str(data['st_name'])              if 'st_name' in data else None
        self.street_type                = str(data['st_type'])              if 'st_type' in data else None
        self.formated_street            = str(data['formattedstreet'])      if 'formattedstreet' in data else None
        self.occured_on                 = str(data['occured_on'])           if 'occured_on' in data else None
        self.hit_and_run                = str(data['hit_run'])              if 'hit_run' in data else None
        self.train_inovled              = str(data['train_involved'])       if 'train_involved' in data else None
        self.fatality                   = str(data['fatality'])             if 'fatality' in data else None
        self.injury                     = str(data['injury'])               if 'injury' in data else None
        self.pedistrian                 = str(data['pedestrian'])           if 'pedestrian' in data else None
        self.at_intersection            = str(data['at_intersection'])      if 'at_intersection' in data else None
        self.closest_street             = str(data['closest_street'])       if 'closest_street' in data else None
        self.manner_of_collision        = str(data['manner_of_collision'])  if 'manner_of_collision' in data else None
        self.surface_condition          = str(data['surface_cond'])         if 'surface_cond' in data else None
        self.surface_type               = str(data['surface_type'])         if 'surface_type' in data else None
        self.road_condition             = str(data['road_condition'])       if 'road_condition' in data else None
        self.road_type                  = str(data['road_type'])            if 'road_type' in data else None
        self.alignment                  = str(data['alignment'])            if 'alignment' in data else None
        self.primary_factor             = str(data['primary_factor'])       if 'primary_factor' in data else None
        self.second_factor              = str(data['second_factor'])        if 'second_factor' in data else None
        self.weather                    = str(data['weather'])              if 'weather' in data else None
        self.location_kind              = str(data['location_kind'])        if 'location_kind' in data else None
        self.relation_roadway           = str(data['relation_roadway'])     if 'relation_roadway' in data else None
        self.access_control             = str(data['access_control'])       if 'access_control' in data else None
        self.lighting                   = str(data['lighting'])             if 'lighting' in data else None
        self.geolocation                = str(data['geolocation'])          if 'geolocation' in data else None


r = requests.get("https://data.brla.gov/resource/epwd-efpa.json?$limit=200000")

data = r.json()

print "Total Number of Records: " + str(len(data))

reported_accidents = {}

for i in range(0, len(data)):
    accident = Accident(data[i])
    if accident.street_name in reported_accidents and accident.occured_on == 'CITY STREET' and accident.fatality == 'X':
        reported_accidents[accident.street_name] += 1
    else:
        reported_accidents[accident.street_name] = 1

count = sorted([(k,v) for (v,k) in reported_accidents.items()], reverse=True)

for k,v in count:
    if k >= 1:
        print "Accidents: " + str(k) + " --- Street: " + str(v)
