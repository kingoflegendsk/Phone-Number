import phonenumbers
from phonenumbers import carrier, geocoder, timezone

mobileNo = input("Entire mobile number with country code: ")
mobileNo = phonenumbers.parse(mobileNo)

# Get timezone a phone number
print(timezone.time_zones_for_number(mobileNo))

# Getting carrier of a phone number
print(carrier.name_for_number(mobileNo, "en"))

# Getting region information
print(geocoder.description_for_number(mobileNo, "en"))

# validating a phone number
print("valid mobile number :", phonenumbers.is_valid_number(mobileNo))

# Checking possibility of a number
print("Checking possibility of numbers :", phonenumbers.is_possible_number(mobileNo))
