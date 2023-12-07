import random
import string

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    # Ensure at least one character type is selected
    if not characters:
        return "Please select at least one character type."

    generated_password = ''.join(random.choice(characters) for _ in range(length))
    return generated_password

# Usage
password = generate_password(12, True, True, True, True)
print(password)
