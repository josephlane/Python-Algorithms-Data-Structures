import re
import requests 
from bs4 import BeautifulSoup

class Owner(object):
    def __init__(self, primary_name, primary_address, all_owners):
        self.primary__name = primary_name
        self.primary_address = primary_address
        self.owners = all_owners

class Property(object):
    def __init__(self):
        self.address = None
        self.legal_description = None
        self.deed_history = None
        self.property_type = None
        self.subdivision = None
        self.owner = None

    def clean_data(self, property_data):
        #property processing
        self.property_type = self.convert_to_text(property_data.find('div',
            attrs={'data-group': 'ptype'}).find_all('span')[1].text)
        self.legal_description = self.convert_to_text(property_data.find('div',
                attrs={'data-group': 'legal'}).find_all('span')[1].text)
        self.address = self.convert_to_text(property_data.find('div',
            attrs={'data-group': 'physicalAddress'}).find_all('span')[1].text)
        deeds = property_data.find_all('table', class_='smallTable')[1]
        subdivision = property_data.find_all('table', class_='mediumTable')[1]
        self.subdivision = self.get_row_data(subdivision)
        self.deed_history = self.get_row_data(deeds)

        #owner process
        owner_data = property_data.find_all('table', class_='mediumTable')[0]
        primary_owner_name = property_data.find('div', attrs={'data-group': 'ownerName'}).find_all('span')[1].text
        primary_owner_address = property_data.find('div', attrs={'data-group': 'mailingAddress'}).find_all('span')[1].text
        all_owners = self.get_row_data(owner_data)
        self.owner = Owner(primary_owner_name, primary_owner_address, all_owners)

    def get_row_data(self, data):
        remove_special_chars = True
        headers = []
        result = []
        for header in data.find_all('th'):
            headers.append(self.convert_to_text(header.text.lower(),
                remove_special_chars))

        for row in data.find_all("tr"):
            if len(row.find_all("td")) > 0:
                result.append({headers[i]:
                    self.convert_to_text(cell.text.lower()) for i, cell in
                    enumerate(row.find_all("td"))})
        #result = [{headers[i]: self.convert_to_text(cell.text.lower()) for i, cell in enumerate(row.find_all("td"))} if len(row.find_all("td")) > 0 for row in data.find_all("tr")]
        return result

    def convert_to_text(self, data, remove_special_chars=False):
        result = data.strip().encode('utf-8')
        if remove_special_chars:
            result = re.sub('[^A-Za-z0-9]+', '', result)
        return result

class Accessor(object):
    def __init__(self, url, params, headers):
        self.url = url
        self.params = params
        self.headers = headers

    def get_property_data(self):
        r = requests.get(self.url, params=self.params, headers=self.headers) 
        soup = BeautifulSoup(r.text, 'html.parser')
        print soup
        return soup

