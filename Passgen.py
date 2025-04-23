import string
import secrets

def generate_password(length=12):
    """
    Generates a random password of specified length with a mix of uppercase
    and lowercase letters, numbers, and special characters.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def generate_multiple_passwords(num_passwords, length=12):
    """
    Generates multiple random passwords.
    """
    passwords = [generate_password(length) for _ in range(num_passwords)]
    return passwords

if __name__ == "__main__":
    try:
        print("Welcome to the Secure Password Generator!")
        print("This script will generate strong, secure passwords.")
        print("Please enter the number of passwords and the desired length.")
        print("---------------------------------------------")
        
        num_passwords = int(input("Enter the number of passwords to generate: "))
        length = int(input("Enter the length of each password: "))
        
        if num_passwords <= 0 or length <= 0:
            raise ValueError("Number of passwords and length must be positive integers.")
        
        passwords = generate_multiple_passwords(num_passwords, length)
        print("\nGenerated Passwords:")
        for idx, password in enumerate(passwords, start=1):
            print(f"Password {idx}: {password}")
    
    except ValueError as ve:
        print(f"Error: {ve}")
