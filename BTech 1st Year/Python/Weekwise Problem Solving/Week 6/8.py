def first_non_repeating_char(string):
    # Create a dictionary to store character counts
    char_count = {}
    
    # Iterate through the string and count occurrences of each character
    for char in string:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    
    # Iterate through the string again to find the first non-repeating character
    for char in string:
        if char_count[char] == 1:
            return char
    
    return None  # Return None if no non-repeating character is found

# Input a string
input_string = input("Enter a string: ")

# Find the first non-repeating character
result = first_non_repeating_char(input_string)

# Output the result
if result:
    print(f"The first non-repeating character is: {result}")
else:
    print("No non-repeating character found.")