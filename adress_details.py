from contact import Contact
import json
import csv
import pandas as pd

class ContactDetails:


    def __init__(self):
        self.contact_list = []
        self.address_dictionary = {}
        #self.json_file = "address_book.json"
        self.csv_file = "address_book.csv"

    def add_contact(self):
        """
        this function for adding new contacts in contact_list
        :return: new added contact
        """
        contact = Contact.create_contact()
        self.contact_list.append(contact)

        df = pd.read_csv('address_book.csv')
        #print(df)
        adf = pd.DataFrame({'FIRST NAME': [contact.first_name],
                        'LAST NAME': [contact.last_name],
                        'ADDRESS': [contact.address],
                        'CITY': [contact.city],
                        'STATE': [contact.state],
                        'ZIP CODE': [contact.zip],
                        'PHONE NUMBER': [contact.phone_number],
                        'EMAIL': [contact.email]})
        adf.to_csv('address_book.csv',mode='a', header=False, index=None)
        #storing all contacts in address_book.csv file
        """with open("address_book.csv", "w") as f:
            for contact in self.contact_list:
                f.write(f"FIRST NAME -> {contact.first_name}\n"
                        f"LAST NAME -> {contact.last_name}\n"
                        f"ADDRESS -> {contact.address}\n"
                        f"CITY -> {contact.city}\n"
                        f"STATE -> {contact.state}\n"
                        f"ZIP CODE -> {contact.zip}\n"
                        f"PHONE NUMBER -> {contact.phone_number}\n"
                        f"EMAIL -> {contact.email}\n\n")"""



    def display_contact(self):
        """
        this function for display all the contacts that are present in contact_list
        :return: all contacts
        """
        contacts = "".join(str(contact) for contact in self.contact_list)
        print(contacts)


    def delete_contact(self):
        """
        In this function we delete whole object of single contact with the help of comparing first_name
        :return: matched object of contact
        """
        delete_first_name = input("Enter first name that you want to delete\n")
        for contact in self.contact_list:
            if contact.first_name == delete_first_name:
                #print(str(contact))
                self.contact_list.remove(contact)
            else:
                print(f"No contact is present with first name {delete_first_name} ")


    def edit_contact(self):
        """
        this function for editing contact with the help of first_name
        :return: edited contact and store in contact_list
        """
        edit_data = input("Enter the first name of user you want to edit\n")

        for contact in self.contact_list:
            if contact.first_name == edit_data:
                user_input = int(input(
                    "Enter the number that you want to edit field in details"
                    " \n 1. First Name 2. Last name 3. Address 4. city 5. state 6.zip 7. Phone number 8.Email \n"))
                if user_input == 1:
                    first_name = input("Enter new first name\n")
                    contact.first_name = first_name
                elif user_input == 2:
                    last_name = input("Enter new last name\n")
                    contact.last_name = last_name
                elif user_input == 3:
                    address = input("Enter new address\n")
                    contact.address = address
                elif user_input == 4:
                    city = input("Enter new city\n")
                    contact.city = city
                elif user_input == 5:
                    state = input("Enter new state\n")
                    contact.state = state
                elif user_input == 6:
                    zip = input("Enter new zip\n")
                    contact.zip = zip
                elif user_input == 7:
                    phone_number = input("Enter new phone number\n")
                    contact.phone_number = phone_number
                elif user_input == 8:
                    email = input("Enter new email\n")
                    contact.email = email
                else:
                    print("Please enter a valid input")
            else:
                print("Please enter a valid name")

