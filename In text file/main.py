import phonenumbers
from phonenumbers import carrier, geocoder, timezone
import opencage
from opencage.geocoder import OpenCageGeocode
import folium
import requests


# NumberPhone and information
Number = input("Enter your phone number: ")
parse = phonenumbers.parse(Number)
pepnumber = phonenumbers.parse(Number)
location = geocoder.description_for_number(pepnumber, "en")

# Operator
service = phonenumbers.parse(Number)

# A phone number may or may not exist
valid = phonenumbers.is_valid_number(parse)

# Continent
timeZone = timezone.time_zones_for_number(parse)

# Can this number exist in theory
possible = phonenumbers.is_valid_number(parse)

# Information about the location of this phone
key = 'b477dddab04e4cd8aee4770631a11192'
# OpenCage Geocoding API: https://opencagedata.com/

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)
myMap.save("location.txt")

with open(file='../information.txt', mode='a', encoding='utf-8') as file:
    file.write(f'Country: {location}\n'
               f'Does this number exist?: {valid}\n'
               f'Could this number exist in theory?:{possible}\n'
               f'{service}\n'
               f'Continent/City: {timeZone}\n'
               f'Operator:{carrier.name_for_number(service, "en")}\n'
               f'{"#" * 20}\n')


# Information displayed in the console
print(location)
print(lng, lat)
print(carrier.name_for_number(service, "en"))
print(''.join(timeZone))
print("Does this number exist?:", valid)
print("Could this number exist in theory?:", possible)
print(service)




