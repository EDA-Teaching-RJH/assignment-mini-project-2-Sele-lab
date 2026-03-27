class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def display(self):
        return f"{self.name} | {self.phone} | {self.email}"
    
class FavouriteContact(Contact):
    def __init__(self, name, phone, email):
        super().__init__(name, phone, email)
        self.favourite = True

import re

