from contact import Contact
import logging

logging.basicConfig(filename="address_book_system.log", filemode="w")
log = logging.getLogger()

class EmptyData(Exception):...
    #Raise when any field is empty
class InvalidLength(Exception):...
    #Raise when mobile number is less than 10 digit or zip code less than 6
class InvalidNumericData(Exception):...
    #Raise when zip code is wrong

class ContactDetails:
    @staticmethod
    def create_contact():
        """
        taking data from user
        :return: contact dictionary as a object
        """
        try:
            first_name = input("Enter first name :-\t")
            if len(first_name) == 0:
                raise EmptyData
            last_name = input("Enter last name :-\t")
            if len(last_name) == 0:
                raise EmptyData
            address = input("Enter address :-\t")
            if len(address) == 0:
                raise EmptyData
            city = input("Enter city :-\t")
            if len(city) == 0:
                raise EmptyData
            state = input("Enter state :-\t")
            if len(state) == 0:
                raise EmptyData
            zip = input("Enter zip code :-\t")
            if not zip.isnumeric():
                raise InvalidNumericData
            elif len(zip) < 6:
                raise InvalidLength
            phone_number = input("Enter phone number :-\t")
            if len(phone_number) < 10:
                raise InvalidLength
            elif not phone_number.isnumeric():
                raise InvalidNumericData
            email = input("Enter email address :-\t")
            if len(email) == 0:
                raise EmptyData

        except EmptyData:
            print("Empty field not allowed")
            log.error("Empty field not allowed")
            return None
        except InvalidLength:
            print("Entered data length is small !!!!")
            log.error("Entered data length is small !!!!")
            return None
        except InvalidNumericData:
            print("This Data should be in numeric")
            log.error("This Data should be in numeric")
            return None
        except Exception:
            print("")
        #finally:
        #    print("Data is entered successfully")

        contact_dict = {
            "first_name": first_name,
            "last_name": last_name,
            "address": address,
            "city": city,
            "state": state,
            "zip": zip,
            "number": phone_number,
            "email": email
        }
        contact = Contact(contact_dict)
        return contact

    @staticmethod
    def display_contact(contact):
        """
        for printing the contact
        :param contact: passing contact object
        :return: str method that contain details of user contact
        """
        print(contact)