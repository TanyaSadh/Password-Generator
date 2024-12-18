import string
import random
import re

# Defining character sets
lc = string.ascii_lowercase    # lowercase letters
uc = string.ascii_uppercase    # uppercase letters
dig = string.digits            # digits
sc = "!@#$%^&*()"               # special characters

# Input for number of passwords
num_pwds = int(input("How many passwords do you want to generate?\n"))

# Creating a list of all possible characters
chars = []
chars.extend(list(lc))
chars.extend(list(uc))
chars.extend(list(dig))
chars.extend(list(sc))

# Function to check if the password is too easy
def is_easy_password(pwd):
    # Check for simple sequential patterns like "1234", "abcd"
    if re.search(r'(0123|1234|2345|3456|4567|5678|6789|abcd|bcde|cdef|defg|efgh|fghi|ghij|hijk|ijkl|jklm|klmn|lmnop|mnopq|nopqr|opqrs|pqrst|qrst)', pwd):
        return True  # Password is too easy
    
    # Check for patterns like "password123" or "name123"
    if re.search(r'password|name|123|1234|qwerty', pwd, re.IGNORECASE):
        return True  # Password is too easy
    
    return False  # Password is not too easy

print("\nGenerated Passwords:")
for i in range(num_pwds):
    while True:
        # Input for the length of each password
        pw_len = int(input(f"Enter the length for password {i + 1} (Max 10):\n"))
        
        # Ensure the password length is less than or equal to 10
        if pw_len <= 10:
            # Generate a random password using choices (with repetition allowed)
            pwd = "".join(random.choices(chars, k=pw_len))
            
            # Validate the password
            if is_easy_password(pwd):
                print("Password is too easy. Please generate a stronger password.")
            else:
                print(f"Password {i + 1}: {pwd}")
                break
        else:
            print("Password length cannot be greater than 10. Please enter a valid length.")
