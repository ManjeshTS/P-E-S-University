def are_anagrams(string1, string2):
    # Remove spaces and punctuation, and convert to lowercase
    clean_string1 = ''.join(char.lower() for char in string1 if char.isalnum())
    clean_string2 = ''.join(char.lower() for char in string2 if char.isalnum())
    
    # Check if sorted characters of both strings are equal
    return sorted(clean_string1) == sorted(clean_string2)

# Input two strings
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Check if the strings are anagrams
if are_anagrams(string1, string2):
    print(f'"{string1}" and "{string2}" are anagrams.')
else:
    print(f'"{string1}" and "{string2}" are not anagrams.')