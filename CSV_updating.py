from tempfile import NamedTemporaryFile
import shutil
import csv
import codecs
import datetime

class Facility:
    """Facility class to handle new facility objects. """
    def __init__(self, facility_name: str, state: str, filename: str = 'Addresses-Billing.csv', new_facility: bool = False, **kwargs):
        self.facility_name = facility_name.title()
        self.filename = filename
        self.new_facility = new_facility
        options = ['name', 'street_1', 'street_2', 'address', 'zip_code', 'website']
        for o in options: # setting default values for acceptable kwargs
            setattr(self, o, None)
        for k, v in kwargs.items():
            if k in self.__dict__: # ensuring every kwarg passed is valid option
                setattr(self, k, v.title())
            else:
                raise KeyError(k)

        def create_csv_entry(self): 
            file = self.filename
            fields = ['facility_name', 'name', 'street_1', 'street_2', 'address', 'zip_code', 'website']
            with codecs.open(file, 'a', encoding='utf8') as csvfile:
                writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n', fieldnames=fields)
                row = ({'facility_name': self.facility_name, 'name': self.name, 'street_1': self.street_1, 
                        'street_2': self.street_2, 'address': self.address, 'zip_code': self.zip_code, 
                        'website': self.website})
                writer.writerow(row)

        if self.new_facility == True:
            self.create_csv_entry() # if facility object is new (unfound in CSV), above create method will get called

def newentry(arg1, **kwargs):
    """For creating a new entry into CSV file, input parameters could be adjusted as needed depending on columns """
    filename = 'customers10-Copy.csv'
    fields = ['name', 'street', 'address', 'zip', 'website']
    with codecs.open(filename, 'a', encoding='utf8') as csvfile:
        writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n', fieldnames=fields)
        name = str(arg1)
        street = ''
        address = ''
        zip_code = ''
        website = ''
        for key, value in kwargs.items():
            if key == 'street':
                street = value
            if key == 'address':
                address = value
            if key == 'zip':
                zip_code = value
            if key == 'website':
                website = value
        row = ({'name': name, 'street': street, 'address': address, 'zip': zip, 'website': website})
        writer.writerow(row)
        print('Done! Alh')

def update(facility: Facility, **kwargs):
    """Updating facility/company data in CSV file, assuming Facility object is used."""
    file = facility.filename
    fields = ['facility_name', 'name', 'street_1', 'street_2', 'address', 'zip_code', 'website']
    with codecs.open(file, 'r+', encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile, fieldnames=fields)
        rows = []
        for row in reader:
            if facility.name == row['facility_name'] and facility.state in row['address']: # confirming facility
                for key, value in kwargs.items():
                    if key in fields: # updating values per given input
                        row[key] = value
            rows.append(row)
        csvfile.seek(0)
        writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n', fieldnames=fields)
        writer.writerows(rows)
        csvfile.truncate()
