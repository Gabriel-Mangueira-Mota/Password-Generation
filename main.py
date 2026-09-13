# gbrzill | Gabriel Mota
import string
import secrets
import pyperclip as clip
import time

password = None

while True:

    # Main menu
    print("\nPassword Generation")
    print("Select an option")
    print("1 | PIN - 1234 - only numbers")
    print("2 | PIN - 123456 - only numbers")
    print("3 | Password - only numbers - custom length")
    print("4 | Password - 10 characters - lowercase, uppercase and numbers")
    print("5 | URL-safe random text")
    print("6 | Alphanumeric password - custom length")
    print("0 | Exit")   

    # Get the user's choice
    escolha = input("\nChoose an option: ")

    # Check if the input is a number
    if not escolha.isdigit():
        print("Error, select a valid option.")
        continue

    escolha = int(escolha)

    # 4-digit PIN
    if escolha == 1:

        # string.digits contains: 0123456789
        alphabet = string.digits

        # Generate 4 random digits
        password = ''.join(
            secrets.choice(alphabet) for _ in range(4)
        )

        # Copy the password directly to the clipboard
        clip.copy(password)

        print("Copied to the clipboard!")
        time.sleep(3)

    # 6-digit PIN
    elif escolha == 2:

        alphabet = string.digits

        # Generate 6 random digits
        password = ''.join(
            secrets.choice(alphabet) for _ in range(6)
        )

        clip.copy(password)

        print("Copied to the clipboard!")
        time.sleep(3)

    # Custom numeric password
    elif escolha == 3:

        value_input = input(
            "Choose how many numbers it will have: "
        )

        if value_input.isdigit():

            value = int(value_input)

            alphabet = string.digits

            # Generate the amount of numbers chosen by the user
            password = ''.join(
                secrets.choice(alphabet) for _ in range(value)
            )

            clip.copy(password)

            print("Copied to the clipboard!")
            time.sleep(3)

        else:

            print("ERROR, only numbers.")

    # 10-character password
    elif escolha == 4:

        # ascii_letters contains uppercase and lowercase letters
        # digits contains numbers from 0 to 9
        alphabet = string.ascii_letters + string.digits

        while True:

            # Generate a 10-character password
            password = ''.join(
                secrets.choice(alphabet) for _ in range(10)
            )

            # Check the password requirements
            if (
                any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3
            ):

                clip.copy(password)

                print("Copied to the clipboard!")
                time.sleep(3)

                break

    # URL-safe random string
    elif escolha == 5:

        # Generate a URL-safe random string
        password = secrets.token_urlsafe(16)

        clip.copy(password)

        print("Copied to the clipboard!")
        time.sleep(3)

    # Custom alphanumeric password
    elif escolha == 6:

        value_input = input(
            "Choose how many characters it will have: "
        )

        if value_input.isdigit():

            value = int(value_input)

            # Letters + numbers
            alphabet = string.ascii_letters + string.digits

            # Generate the amount of characters chosen by the user
            password = ''.join(
                secrets.choice(alphabet) for _ in range(value)
            )

            clip.copy(password)

            print("Copied to the clipboard!")
            time.sleep(3)

        else:

            print("ERROR, only numbers.")

    # Exit
    elif escolha == 0:

        print("Goodbye!")
        break

    # Invalid option
    else:

        print("Error, select a correct option.")