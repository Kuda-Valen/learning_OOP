from abc import ABC, abstractmethod

class SendNofication:
    def __init__(self):
        ...


class Feature:
    def __init__(self, user_data, message, method):
        self.user_data = user_data
        self.message = message
    
class User:
    def __init__(self, name: str, email: str, phone: str, is_active=True):
        self.name = name
        self.email = email
        self.phone = phone
        self.is_active = is_active
        
    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self, value):
        if not value.startwith("+"):
            raise ValueError("Phone numbers must start with a country code (e.g., +27)")
        self._phone = value

if __name__ == "__main__":

    while True:
        print("1. Send a message")
        print("2. Exit")

        option = int(input("Choose an option: "))


