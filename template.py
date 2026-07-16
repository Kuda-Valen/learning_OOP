from abc import ABC, abstractmethod

class User:
    def __init__(self, name, email, phone, is_active=True):
        self.name = name
        self.email = email
        self._phone = phone  # Protected attribute (Encapsulation)
        self.is_active = is_active

    # Encapsulation: We control access to phone validation
    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        if not value.startswith("+"):
            raise ValueError("Phone numbers must start with a country code (e.g., +1)")
        self._phone = value


class NotificationChannel(ABC):  # Abstraction
    @abstractmethod
    def send(self, user, message):
        """Each subclass must implement its own sending logic."""
        pass
    
    def log_notification(self, channel_name, recipient):
        """Common code can be shared here (Inheritance)."""
        print(f"[LOG] Notification successfully sent via {channel_name} to {recipient}.")