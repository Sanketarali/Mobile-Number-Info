import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier
number='+919740481350'
phone_number=phonenumbers.parse(number)

# Fetch the country of a mobile number
print(geocoder.description_for_number(phone_number,'en'))


# Fetch the time zone of a mobile number
print(timezone.time_zones_for_number(phone_number))


# Fetch the service provider of a mobile number
print(carrier.name_for_number(phone_number,'en'))



