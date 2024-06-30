import random
import string
import argparse

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character set must be selected")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    parser = argparse.ArgumentParser(description='Generate a random password with customizable length and complexity.')
    parser.add_argument('-l', '--length', type=int, required=True, help='Length of the password')
    parser.add_argument('-u', '--uppercase', action='store_true', help='Include uppercase letters')
    parser.add_argument('-lc', '--lowercase', action='store_true', help='Include lowercase letters')
    parser.add_argument('-d', '--digits', action='store_true', help='Include digits')
    parser.add_argument('-s', '--special', action='store_true', help='Include special characters')

    args = parser.parse_args()

    try:
        password = generate_password(
            args.length, 
            args.uppercase, 
            args.lowercase, 
            args.digits, 
            args.special
        )
        print(f'Generated Password: {password}')
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()