class SendNofication:
    def __init__(self):
        ...


class Feature:
    def __init__(self, user_data, message, method):
        self.user_data = user_data
        self.message = message
    
class User:
    def __init__(self, name: str, email: str, phone: str, is_active: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.is_active = is_active
    
        name = input("\nEnter Name: ").strip()
        email = input("Enter Email: ").strip()
        phone = input("Enter Phone: ").strip()
        active_input = input("Is user Active [Y/N]: ").strip().lower()

        if active_input == 'y':
            is_active = True
        
        else:
            is_active = False
        
        user = (name, email, phone, is_active)


