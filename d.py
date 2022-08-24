import phonenumbers
from phonenumbers import geocoder
from test import number
import folium

Key1 = 'f81fcb17cbb449508def1100851f3bc2'
ch_number = phonenumbers.parse(number)

yourLocation = geocoder.description_for_number(ch_number, "en")
print(yourLocation)

from phonenumbers import carrier

service_number = phonenumbers.parse(number)
print(carrier.name_for_number(service_number, "en"))

from opencage.geocoder import OpenCageGeocode

geocoder = OpenCageGeocode(Key1)
Query = str(yourLocation)
results = geocoder.geocode(Query)
#print(results)

lat = results[0]['geometry']['lat']

lng = results[0]['geometry']['lng']

print(lat,lng)
