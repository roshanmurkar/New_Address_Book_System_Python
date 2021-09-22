from adress_details import ContactDetails
import logging


log = logging.getLogger()

if __name__ == "__main__":
    print("******** Welcome to Address Book Management System *********")
    new_contact = ContactDetails()

    while True:
        try:
            user_choice = int(input(
                "Choose any operation and enter that number"
                "\n 1.Add New Contact "
                "\n 2.Display the Contact "
                "\n 3.Edit Existing Contact "
                "\n 4.Delete the contact"
                "\n 5.Exit\n"))

            """option_dict = {
                    1: new_contact.add_contact(),
                    2: new_contact.display_contact(),
                    3: new_contact.edit_contact(),
                    4: new_contact.delete_contact()
                }
                option_dict.get(user_choice)"""

            if user_choice == 1:
                new_contact.add_contact()
            elif user_choice == 2:
                new_contact.display_contact()
            elif user_choice == 3:
                new_contact.edit_contact()
            elif user_choice == 4:
                new_contact.delete_contact()
            elif user_choice == 5:
                print("Thank you :)")
                exit(0)
            else:
                log.warning("Invalid option")
        except ValueError:
            logging.warning("Invalid Option selected")
        except Exception as e:
            print("")


            """
            json
            {"Addressbook1":[{"contact_name:{Contact values}},
            "contact_name2":{{Contact values}},...],
            "Addressbook2":[...]}
            """