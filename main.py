from adress_details import ContactDetails

if __name__ == "__main__":
    print("******** Welcome to Address Book Management System *********")
    new_contact = ContactDetails()
    contact = new_contact.create_contact()
    new_contact.display_contact(contact)