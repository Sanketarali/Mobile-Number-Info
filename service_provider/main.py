import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier
number='+919740481350'
phone_number=phonenumbers.parse(number)
print(geocoder.description_for_number(phone_number,'en'))
print(timezone.time_zones_for_number(phone_number))
print(carrier.name_for_number(phone_number,'en'))



