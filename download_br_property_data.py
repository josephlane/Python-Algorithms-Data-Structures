import time
from download_property_data import * 

details_url = "http://ebrassessor.azurewebsites.net/Details"
details_params = {"parcelNumber": ""}
sub_div_url = "https://data.brla.gov/resource/bkhi-fpvp.json"
parcel_url = "http://ebrassessor.azurewebsites.net/api/Search"
parcel_params = {"value": "","fieldType": "4", "taxyear": ""}
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'}
params = "884022/2017"
subdivisions = requests.get(sub_div_url).json()
results = []
for sub_division in subdivisions:
    sub_name = sub_division['subd_name'].strip()
    parcel_params['value'] = sub_name
    print "Processing Subdivision: {0}".format(sub_name)
    parcels = requests.get(parcel_url, params=parcel_params).json()
    for parcel in parcels:
        print "Retrieving Property Data for Parcel: {0}".format(parcel['parcelNumber'])
        details_params['parcelNumber'] = parcel['parcelNumber']
        accessor = Accessor(details_url, details_params, headers)
        property_data = accessor.get_property_data()
        results.append(property_data)
        time.sleep(1)
    break
