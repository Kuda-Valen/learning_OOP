# --- INSTEAD OF THIS MESSY SCRIPT ---

def send_notification(user_data, message, method):
    # Messy validation mixed in with sending logic
    if not user_data.get("is_active"):
        print(f"Skipping inactive user: {user_data['name']}")
        return

    # Email Logic
    if method == "email":
        if "@" not in user_data.get("email", ""):
            print("Invalid email address!")
            return
        # Pretend we are calling an external Email API
        print(f"Sending EMAIL to {user_data['email']}: [Subject: Alert] {message}")
        print("Saving email log to database...")

    # SMS Logic
    elif method == "sms":
        phone = user_data.get("phone", "")
        if not phone.startswith("+"):
            print("Invalid phone number format!")
            return
        # Pretend we are calling an SMS Gateway (like Twilio)
        print(f"Sending SMS to {phone}: {message}")
        print("Saving SMS log to database...")

    # WhatsApp Logic
    elif method == "whatsapp":
        phone = user_data.get("phone", "")
        if not phone.startswith("+"):
            print("Invalid phone number format!")
            return
        # Pretend we are calling the Meta WhatsApp Business API
        print(f"Sending WHATSAPP to {phone}: {message}")
        print("Saving WhatsApp log to database...")
        
    else:
        print(f"Unknown notification method: {method}")

# --- Execution ---
user_1 = {"name": "Alice", "email": "alice@example.com", "phone": "+123456789", "is_active": True}
user_2 = {"name": "Bob", "phone": "555-0199", "is_active": True} # Invalid phone format

send_notification(user_1, "Your package has shipped!", "email")
send_notification(user_1, "Your package has shipped!", "sms")
send_notification(user_2, "Your package has shipped!", "sms") # Will fail validation

print(f"\nUser 1's info: {user_1}")
print(f"\nUser 2's info: {user_2}")