import json
import random
import re
import string

VAULT_TIEDOSTO = "vault.txt"

def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def check_password_strength(password):
    if (len(password) >= 8 and
        any(char.isdigit() for char in password) and
        any(char.isupper() for char in password) and
        any(char.islower() for char in password) and
        any(char in string.punctuation for char in password)):
        return "Salasana on vahva."
    return "Salasana on heikko."

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

encrypted_passwords = []
websites = []
usernames = []

def add_password(site, username, password):
    encrypted_password = caesar_encrypt(password, 3)

    encrypted_passwords.append(encrypted_password)
    websites.append(site)
    usernames.append(username)

    print(f"Salasana tallennettu: {site} -> Käyttäjä: {username}")

def get_password(site):
    for i in range(len(websites)):
        if websites[i] == site:
            decrypted_password = caesar_decrypt(encrypted_passwords[i], 3)
            print(f"Sivusto: {websites[i]} | Käyttäjä: {usernames[i]} | Salasana: {decrypted_password}")
            return
    print("Sivustoa ei löytynyt.")

def save_passwords():
    magic = {}
    magic["site"] = websites
    magic["username"] = usernames
    magic["password"] = encrypted_passwords

    with open(VAULT_TIEDOSTO, "w") as tiedosto:
        json.dump(magic, tiedosto)

def load_passwords():
    with open(VAULT_TIEDOSTO, "r") as tiedosto:
        data = json.load(tiedosto)
    global websites
    global usernames
    global encrypted_passwords
    websites = data["site"]
    usernames = data["username"]
    encrypted_passwords = data["password"]

    

def main():
    while True:

        print("\n1. Lisää salasana")
        print("2. Hae salasana")
        print("3. Luo vahva salasana")
        print("4. Tallenna salasanat")
        print("5. Lataa salasanat")
        print("6. Lopeta")
        valinta = input("Valitse toiminto: ")

        if valinta == "1":
            site = input("Sivuston nimi: ")
            username = input("Käyttäjänimi: ")
            password = input("Salasana: ")
            print("Salasanan vahvuus:", check_password_strength(password))
            add_password(site, username, password)
        elif valinta == "2":
            site = input("Sivuston nimi: ")
            get_password(site)
        elif valinta == "3":
            length = int(input("Salasanan pituus (numeroina): "))
            print("Satunnainen vahva salasana:", generate_random_password(length))
        elif valinta == "6":
            break
        elif valinta == "4":
            save_passwords()
            print("Salasanat tallennettu onnistuneesti!")
        elif valinta == "5":
            load_passwords()
            print("Salasanat ladattu onnistuneesti!")
        else:
            print("Virheellinen valinta, yritä uudelleen.")

if __name__ == "__main__":
    main()
