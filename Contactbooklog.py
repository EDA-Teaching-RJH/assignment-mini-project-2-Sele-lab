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

def valid_email(email):
    return re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email) is not None


def valid_phone(phone):
    return re.fullmatch(r"\d{10}", phone) is not None

def search_contacts(contacts, keyword):
    return [c for c in contacts if re.search(keyword, c.name, re.IGNORECASE)]

def save_contacts(contacts):
    with open("contacts.txt", "w") as f:
        for c in contacts:
            f.write(f"{c.name},{c.phone},{c.email}\n")

def load_contacts():
    contacts = []
    try:
        with open("contacts.txt", "r") as f:
            for line in f:
                name, phone, email = line.strip().split(",")
                contacts.append(Contact(name, phone, email))
    except FileNotFoundError:
        pass
    return contacts

    