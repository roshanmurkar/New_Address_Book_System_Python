import logging
import re
logging.basicConfig(filename="address_book_system.log", filemode="w")
log = logging.getLogger()

class EmptyData(Exception):...
    #Raise when any field is empty
class InvalidLength(Exception):...
    #Raise when mobile number is less than 10 digit or zip code less than 6
class InvalidNumericData(Exception):...
    #Raise when zip code or mobile number  is wrong
class ValidationError(Exception):
    #Raise when regex pattern is not match
    def __init__(self,message):
        self.message = message

class Contact:
    def __init__(self, contact):
        """
        getting values in dictionary
        :param contact: it contain dictionary
        """
        self.first_name = contact.get("first_name")
        self.last_name = contact.get("last_name")
        self.address = contact.get("address")
        self.city = contact.get("city")
        self.state = contact.get("state")
        self.zip = contact.get("zip")
        self.phone_number = contact.get("phone_number")
        self.email = contact.get("email")

    def __str__(self) -> str:

        return f"First Name = {self.first_name} \n" \
               f"Last Name = {self.last_name} \n" \
               f"Address = {self.address} \n" \
               f"City = {self.city} \n" \
               f"State = {self.state} \n" \
               f"Zip = {self.zip} \n" \
               f"Phone Number = {self.phone_number} \n" \
               f"Email = {self.email}\n\n"

    @staticmethod
    def create_contact():
        first_name = input("Enter first name:\t")
        try:
            if re.fullmatch('^[A-Za-z]{2,}$',first_name):
                first_name = first_name
            else:
                raise ValidationError("First Name is not valid")
        except ValidationError as e:
            print(e.message)

        last_name = input("Enter last name:\t")
        try:
            if re.fullmatch('^[A-Za-z]{2,}$',last_name):
                last_name = last_name
            else:
                raise ValidationError("First Name is not valid")
        except ValidationError as e:
            print(e.message)

        address = input("Enter address:\t")
        try:
            if re.fullmatch('^[A-Za-z ]{2,}$',address):
                address = address
            else:
                raise ValidationError("Address is not valid")
        except ValidationError as e:
            print(e.message)

        city = input("Enter city:\t")
        try:
            if re.fullmatch('^[A-Za-z]{2,}$',city):
                city = city
            else:
                raise ValidationError("City is not valid")
        except ValidationError as e:
            print(e.message)

        state = input("Enter state:\t")
        try:
            if re.fullmatch('^[A-Za-z]{2,}$',state):
                state = state
            else:
                raise ValidationError("State is not valid")
        except ValidationError as e:
            print(e.message)

        zip = input("Enter zip code:\t")
        try:
            if re.fullmatch('^[0-9]{6,}$',zip):
                zip = zip
            else:
                raise ValidationError("Zip code is not valid")
        except ValidationError as e:
            print(e.message)

        phone_number = input("Enter phone number:\t")
        try:
            if re.fullmatch('^[0-9]{10,}$',phone_number):
                phone_number = phone_number
            else:
                raise ValidationError("Phone number is not valid")
        except ValidationError as e:
            print(e.message)

        email = input("Enter email id:\t")
        try:
            if re.fullmatch('[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+',email):
                email = email
            else:
                raise ValidationError("Email is not valid")
        except ValidationError as e:
            print(e.message)


        contact_dict = {
            "first_name": first_name,
            "last_name": last_name,
            "address": address,
            "city": city,
            "state": state,
            "zip": zip,
            "phone_number": phone_number,
            "email": email
        }
        contact = Contact(contact_dict)
        return contact
