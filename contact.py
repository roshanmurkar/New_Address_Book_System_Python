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
               f"Email = {self.email}"