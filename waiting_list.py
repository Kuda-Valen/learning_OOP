"""
So we are designing a ticked tracking system. a customer comes to buy a ticket of who they want to see, and we sell them a ticked number that is linked to thier artists
"""

# Artist Arrays
post_malone = []
travis_scott = []
drake = []
tickets = []
customers =[]

class Customer:
    def __init__(self, name, last_name, phone, ticket_no):
        self.name = name 
        self.last_name = last_name
        self.phone = phone
        self.ticket_no = ticket_setter()

        customer = (name, last_name, phone, ticket_no)

def ticket_setter():
    global tickets

    last_no = tickets[-1]
    ticket_no = last_no + 1
    return ticket_no

if __name__ == "__main__":
    customer = Customer()

    while True:
        print("\n== Ticket System ==\n")
        print("1. Purchase a Ticket")
        print("2. Print All Customers")
        print("3. Print Artist Tickets Sold")
        print("5. Exit")

        try:
            option = int(input("Choose an option: "))

            if option == 1:
                customer()
            
            elif option == 2:
                ...

            elif option == 3:
                ...
            
            elif option == 4:
                ...
            
            elif option == 5:
                print("\nExiting System...")
            
            else:
                print("\nInvalid input!!.. Choose a valid optoin:")
        
        except ValueError as e:
            print(f"\nEncountered an input error: {e}")