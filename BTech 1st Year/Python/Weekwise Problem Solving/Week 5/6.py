from datetime import datetime, timedelta

# List to store rental information
rental_data = []

# Function to add a new rental entry
def add_rental(vehicle_type, reg_no, name, phone_no, borrow_date, expected_return, rent_per_day, extra_rent_per_hour, deposit, in_hand):
    rental_entry = {
        "Vehicle": {"Type": vehicle_type, "Reg_no": reg_no},
        "Borrower Details": {"Name": name, "Phone_no": phone_no},
        "Rent Details": {
            "Borrow_date": borrow_date,
            "Expected_return": expected_return,
            "Rent_per_day": rent_per_day,
            "Extra_rent_per_hour": extra_rent_per_hour,
            "Deposit": deposit,
            "In_hand": in_hand,
        }
    }
    rental_data.append(rental_entry)

# Function to calculate and update rent details
def calculate_rent(reg_no, actual_return):
    for entry in rental_data:
        if entry["Vehicle"]["Reg_no"] == reg_no:
            rent_details = entry["Rent Details"]
            borrow_date = datetime.strptime(rent_details["Borrow_date"], "%d/%m/%Y %H.%M.%S %p")
            expected_return = datetime.strptime(rent_details["Expected_return"], "%d/%m/%Y %H.%M.%S %p")
            actual_return_date = datetime.strptime(actual_return, "%d/%m/%Y %H.%M.%S %p")
            
            # Calculate overdue time
            if actual_return_date > expected_return:
                overdue = actual_return_date - expected_return
                overdue_days = overdue.days
                overdue_hours = overdue.seconds // 3600
                total_extra_rent = overdue_days * rent_details["Rent_per_day"] + overdue_hours * rent_details["Extra_rent_per_hour"]
                print(f"Overdue Charges: Rs {total_extra_rent}")
            else:
                print("Returned on time. No extra charges.")
            
            rent_details["In_hand"] = False
            break
    else:
        print("Vehicle with the given registration number")