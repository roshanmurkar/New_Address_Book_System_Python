from contact import Contact


class ContactDetails:
    contact_list = []

    def add_contact(self):
        contact = Contact.create_contact()
        self.contact_list.append(contact)

    def display_contact(self):
        contacts = "".join(str(contact) for contact in self.contact_list)
        print(contacts)

    def edit_contact(self):
        edit_data = input("Enter the first name of user you want to edit\n")
        for contact in self.contact_list:
            if contact.first_name == edit_data:
                choice = int(input(
                    "Enter the number that you want to edit field in details"
                    " \n 1. First Name 2. Last name 3. Address 4. city 5. state 6.zip 7. Phone number 8.Email\n"))
                if choice == 1:
                    first_name = input("Enter new first name\n")
                    contact.first_name = first_name
                elif choice == 2:
                    last_name = input("Enter new last name\n")
                    contact.last_name = last_name
                elif choice == 3:
                    address = input("Enter new address\n")
                    contact.address = address
                elif choice == 4:
                    city = input("Enter new city\n")
                    contact.city = city
                elif choice == 5:
                    state = input("Enter new state\n")
                    contact.state = state
                elif choice == 6:
                    zip = input("Enter new zip\n")
                    contact.zip = zip
                elif choice == 7:
                    phone_number = input("Enter new phone number\n")
                    contact.phone_number = phone_number
                elif choice == 8:
                    email = input("Enter new email\n")
                    contact.email = email
                else:
                    print("Please enter a valid input")
            else:
                print("Please enter a valid name")
