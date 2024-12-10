def are_isomorphic(s, t):
    # If the strings have different lengths, they cannot be isomorphic
    if len(s) != len(t):
        return False
    
    # Dictionaries to store mappings from s to t and t to s
    mapping_s_to_t = {}
    mapping_t_to_s = {}
    
    # Iterate through characters of both strings
    for char_s, char_t in zip(s, t):
        # Check if there's already a mapping for char_s in s to char_t in t
        if char_s in mapping_s_to_t:
            if mapping_s_to_t[char_s] != char_t:
                return False
        else:
            mapping_s_to_t[char_s] = char_t
        
        # Check if there's already a mapping for char_t in t to char_s in s
        if char_t in mapping_t_to_s:
            if mapping_t_to_s[char_t] != char_s:
                return False
        else:
            mapping_t_to_s[char_t] = char_s
    
    return True

# Input two strings
s = input("Enter the first string: ")
t = input("Enter the second string: ")

# Check if the strings are isomorphic
if are_isomorphic(s, t):
    print(f'"{s}" and "{t}" are isomorphic.')
else:
    print(f'"{s}" and "{t}" are not isomorphic.')