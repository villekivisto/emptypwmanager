import json

def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

encrypted_passwords = []
websites = []
usernames = []

def add_password():
    """
    Add a new password to the password manager.

    This function prompts the user for the website, username, and password and stores them
    to lists with the same index.

    Returns:
        None
    """
    website = input("Enter website: ")
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    encrypted_password = caesar_encrypt(password, 3)
    websites.append(website)
    usernames.append(username)
    encrypted_passwords.append(encrypted_password)
    print("Password added successfully!")

def get_password():
    """
    Retrieve a password for a given website.

    This function prompts the user for the website name and
    then displays the username and decrypted password for that website.

    Returns:
        None
    """
    website = input("Enter website: ")
    if website in websites:
        index = websites.index(website)
        decrypted_password = caesar_decrypt(encrypted_passwords[index], 3)
        print(f"Username: {usernames[index]}\nPassword: {decrypted_password}")
    else:
        print("Website not found.")

def save_passwords():
    """
    Save the password vault to a file.

    This function saves passwords, websites, and usernames to a text
    file named "vault.txt" in a structured format.

    Returns:
        None
    """
    data = {
        "websites": websites,
        "usernames": usernames,
        "passwords": encrypted_passwords
    }
    with open("vault.txt", "w") as file:
        json.dump(data, file)
    print("Passwords saved successfully!")

def load_passwords():
    """
    Load passwords from a file into the password vault.

    This function loads passwords, websites, and usernames from a text
    file named "vault.txt" and populates the respective lists.

    Returns:
        None
    """
    global websites, usernames, encrypted_passwords
    try:
        with open("vault.txt", "r") as file:
            data = json.load(file)
            websites = data["websites"]
            usernames = data["usernames"]
            encrypted_passwords = data["passwords"]
        print("Passwords loaded successfully!")
    except FileNotFoundError:
        print("No saved passwords found.")

def main():
    """
    Implement the user interface for the password manager.

    This method provides a menu-driven interface for users to interact
    with the password manager.

    Returns:
        None
    """
    while True:
        print("\nPassword Manager Menu:")
        print("1. Add Password")
        print("2. Get Password")
        print("3. Save Passwords")
        print("4. Load Passwords")
        print("5. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_password()
        elif choice == "2":
            get_password()
        elif choice == "3":
            save_passwords()
        elif choice == "4":
            load_passwords()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
