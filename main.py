import phonenumbers
from test import number

from phonenumbers import geocoder #geocoder-builtin package
ch_number = phonenumbers.parse(number, "CH")
#created variable which calls phonenumbers package
#CH -> C - Country, H - History
print(geocoder.description_for_number(ch_number, "en"))
#called geocoder and got description for the number

#Now to get service provider of number
#call carrier for getting service provider name

from phonenumbers import carrier
service_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number, "en"))
#called carrier while printing