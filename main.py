import random
import string

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
        return "Vahva"
    return "Heikko"

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

passwords = {}

def add_password(site, username, password):
    encrypted_password = caesar_encrypt(password, 3)
    passwords[site] = (username, encrypted_password)
    print(f"Salasana tallennettu: {site} -> Käyttäjä: {username}")

def get_password(site):
    if site in passwords:
        username, encrypted_password = passwords[site]
        decrypted_password = caesar_decrypt(encrypted_password, 3)
        print(f"Sivusto: {site} | Käyttäjä: {username} | Salasana: {decrypted_password}")
    else:
        print("Sivustoa ei löytynyt.")

def main():
    while True:
        print("\n1. Lisää salasana")
        print("2. Hae salasana")
        print("3. Luo vahva salasana")
        print("4. Lopeta")
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
        elif valinta == "4":
            break
        else:
            print("Virheellinen valinta, yritä uudelleen.")

if __name__ == "__main__":
    main()
