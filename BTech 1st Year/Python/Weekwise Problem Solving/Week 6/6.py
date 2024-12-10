bookings = {
    "MovieA": {"A1", "A2", "A3"},
    "MovieB": {"B1", "B2"},
    "MovieC": {"C1", "C2", "C3"}
}

def process_bookings(bookings):
    while True:
        # Input format: "CustomerName-MovieName-SeatNumber"
        user_input = input("Enter booking details (or type 'exit' to stop): ").strip()

        if user_input.lower() == "exit":
            break
        
        try:
            # Split the input string
            customer_name, movie_name, seat_number = user_input.split("-")
        except ValueError:
            print("Invalid input format. Please use the format 'CustomerName-MovieName-SeatNumber'.")
            continue
        
        # Ensure movie name exists in the dictionary
        if movie_name not in bookings:
            bookings[movie_name] = set()  # Initialize new movie with an empty set
        
        # Check for duplicate bookings
        if seat_number in bookings[movie_name]:
            print(f"Error: Seat {seat_number} for movie '{movie_name}' is already booked.")
        else:
            bookings[movie_name].add(seat_number)  # Add seat to the set
            print(f"Booking successful for {customer_name} - Movie: {movie_name}, Seat: {seat_number}")
    
    # Display final bookings
    print("\nFinal Bookings:")
    for movie, seats in bookings.items():
        print(f"Movie: {movie}, Booked Seats: {', '.join(seats)}")


# Process the pre-existing bookings
process_bookings(bookings)