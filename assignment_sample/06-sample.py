# Airport Boarding System - Starter Code


# -----------------------------
# Global Data
# -----------------------------

passengers = ["Alice", "Bob", "Chris", "Diana", "Eric"]
tickets = ["A", "B", "B", "C", "A"]
checked_in = [False, True, True, False, True]
bags = [1, 2, 2, 1, 2]

boarded = []

boarding_attempts = 0


# -----------------------------
# Functions
# -----------------------------

def find_passenger(name):
    # Search through the passengers list for the given name.
    # If the passenger is found, return their index.
    # If the passenger is not found, return -1.

    pass


def check_baggage(index):
    # Check the number of bags for the passenger at the given index.
    # A passenger is allowed to check in if they have 2 bags or fewer.
    # Return True if the baggage is allowed.
    # Otherwise, return False.

    pass


def check_in():
    # Ask the user to enter a passenger name.
    # Call find_passenger() to find that passenger.
    # If the passenger does not exist, display an error message.
    # If the passenger is already checked in, display a message.
    # Otherwise, call check_baggage().
    # If the baggage is allowed, change the passenger's checked_in status to True.

    pass


def can_board(index):
    # Increase the global boarding_attempts variable by 1.
    # Check whether the passenger is checked in.
    # Check whether the passenger has already boarded.
    # Return True only if the passenger is allowed to board.
    # Otherwise, return False.

    pass


def board_group(ticket_type):
    # Loop through all passengers.
    # Find passengers whose ticket matches ticket_type.
    # For each matching passenger, call can_board().
    # If can_board() returns True, add the passenger's name to boarded.

    pass


def board_passengers():
    # Board passengers based on ticket priority.
    # First call board_group() for ticket A.
    # Then call board_group() for ticket B.
    # Finally call board_group() for ticket C.

    pass


def show_passenger_status():
    # Ask the user to enter a passenger name.
    # Call find_passenger() to find the passenger.
    # If the passenger does not exist, display an error message.
    # Otherwise, display their name, ticket, number of bags,
    # check-in status, and boarding status.

    pass


def all_boarded():
    # Check every passenger to determine whether they have boarded.
    # If at least one passenger has not boarded, return False.
    # If every passenger has boarded, return True.

    pass


def show_all_status():
    # Loop through every passenger.
    # Display each passenger's name, ticket, number of bags,
    # check-in status, and boarding status.
    # Also display the total number of boarding attempts.

    pass


# -----------------------------
# Main Program
# -----------------------------

def main():

    while not all_boarded():

        print("\n----------------------------")
        print("Airport Boarding System")
        print("----------------------------")
        print("1. Check In Passenger")
        print("2. Board Passengers")
        print("3. Passenger Status")

        try:
            choice = int(input("Enter choice: "))

        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            check_in()

        elif choice == 2:
            board_passengers()

        elif choice == 3:
            show_passenger_status()

        else:
            print("Invalid choice.")

    print("\nAll passengers have boarded!")
    show_all_status()


main()