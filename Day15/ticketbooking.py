# Custom Exception for full booking
class BookingFullError(Exception):
    def __init__(self, message="All seats are booked. No more reservations available."):
        self.message = message
        super().__init__(self.message)


# Railway Reservation System Class
class RailwayReservation:
    def __init__(self, total_seats=5):
        # Total available seats 
        self.total_seats = total_seats
        self.booked_tickets = []

    # Book a ticket
    def book_ticket(self, name, destination, seat_type):
        try:
            # Validate passenger name
            if not name or name.isnumeric():
                raise ValueError("Invalid passenger name. Name must be alphabetic.")

            # Validate seat type
            seat_types = ["Sleeper", "AC", "General"]
            if seat_type not in seat_types:
                raise IndexError("Invalid seat type selection.")

            # Check if seats available
            if len(self.booked_tickets) >= self.total_seats:
                raise BookingFullError()

            # Create ticket dictionary
            ticket = {
                "Name": name,
                "Destination": destination,
                "Seat Type": seat_type
            }
            self.booked_tickets.append(ticket)
            print(f"Ticket booked successfully for {name} to {destination} ({seat_type})")

        except ValueError as e:
            print(e)
        except IndexError as e:
            print(e)
        except BookingFullError as e:
            print(e)

    # Cancel a ticket
    def cancel_ticket(self, name):
        found = False
        for ticket in self.booked_tickets:
            if ticket["Name"].lower() == name.lower():
                self.booked_tickets.remove(ticket)
                found = True
                print(f"Ticket for {name} has been cancelled.")
                break
        if not found:
            print("No ticket found for the given name.")

    # View all booked tickets
    def view_tickets(self):
        if not self.booked_tickets:
            print("No tickets booked yet.")
        else:
            print("\nBooked Tickets:")
            for i, ticket in enumerate(self.booked_tickets, start=1):
                print(f"{i}. Name: {ticket['Name']}, Destination: {ticket['Destination']}, Seat: {ticket['Seat Type']}")


# --- Menu-driven Program ---
def main():
    system = RailwayReservation(total_seats=5)

    while True:
        print("\n===== RAILWAY RESERVATION SYSTEM =====")
        print("1. Book a Ticket")
        print("2. Cancel a Ticket")
        print("3. View All Tickets")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter passenger name: ").strip()
            destination = input("Enter destination: ").strip()
            print("Seat Types: Sleeper, AC, General")
            seat_type = input("Enter seat type: ").strip().title()
            system.book_ticket(name, destination, seat_type)

        elif choice == "2":
            name = input("Enter passenger name to cancel ticket: ").strip()
            system.cancel_ticket(name)

        elif choice == "3":
            system.view_tickets()

        elif choice == "4":
            print("Thank you for using the Railway Reservation System!")
            break

        else:
            print("Invalid choice. Please select from 1 to 4.")


if __name__ == "__main__":
    main()
