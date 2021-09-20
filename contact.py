import logging

log = logging.getLogger()
class EmptyData(Exception):...
    #Raise when any field is empty
class InvalidLength(Exception):...
    #Raise when mobile number is less than 10 digit or zip code less than 6
class InvalidNumericData(Exception):...
    #Raise when zip code or mobile number  is wrong

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
        self.phone_number = contact.get("number")
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
        try:

            first_name = input("Enter first name:\t")
            last_name = input("Enter last name:\t")
            address = input("Enter address:\t")
            city = input("Enter city:\t")
            state = input("Enter state:\t")
            zip = input("Enter zip code:\t")
            phone_number = input("Enter phone number:\t")
            email = input("Enter email id:\t")

            if len(first_name) == 0 or \
                    len(last_name) == 0 or \
                    len(address) == 0 or \
                    len(city) == 0 or \
                    len(state) == 0 or \
                    len(email) == 0:
                raise EmptyData
            elif not zip.isnumeric() or not phone_number.isnumeric():
                raise InvalidNumericData
            elif len(zip) < 6 or len(phone_number) < 10:
                raise InvalidLength

        except EmptyData:
            log.warning("Data is empty")
            return None
        except InvalidNumericData:
            log.warning("Data is not numeric")
            return None
        except InvalidLength:
            log.warning("length of data is small")
            return None

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
