import random

def generate_password(length, chars):
    password = ""
    for _ in range(length):
        password += random.choice(chars)
    return password

def get_valid_input(prompt, min_value=1):
    while True:
        try:
            value = int(input(prompt))
            if value < min_value:
                print(f"Please enter a number greater than or equal to {min_value}.")
            else:
                return value
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

def main():
    print("\nWelcome to your password generator!")

    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*().,?'

    # Get valid user inputs
    num_passwords = get_valid_input("\nAmount of passwords to generate: ")
    password_length = get_valid_input("Input your password length: ")

    print("\nHere are your passwords:")

    for _ in range(num_passwords):
        print(generate_password(password_length, chars))

if __name__ == "__main__":
    main()
