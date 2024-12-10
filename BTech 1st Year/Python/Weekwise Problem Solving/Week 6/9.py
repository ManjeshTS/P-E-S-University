def password_validator(password):
    # Check if the password is at least 8 characters long
    if len(password) < 8:
        print("Invalid password: Must be at least 8 characters long.")
        return False
    
    # Initialize flags for uppercase, lowercase, and number
    has_upper = False
    has_lower = False
    has_digit = False
    
    # Check each character in the password
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
    
    # Check if all conditions are met
    if has_upper and has_lower and has_digit:
        return "Valid password"
    else:
        print("Invalid password: Must contain at least 1 uppercase letter, 1 lowercase letter, and 1 number.")
        return False

# Input a password
password = input("Enter a password: ")

# Validate the password
result = password_validator(password)

# Print the result
if result:
    print(result)