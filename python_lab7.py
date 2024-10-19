alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def vigenere_sq():
    for i in range(len(alphabet)):
        shifted = alphabet[i:] + alphabet[:i]
        formatted_row = f"{alphabet[i]}|{'|'.join(shifted)}|"
        print(formatted_row)

vigenere_sq()

def letter_to_index(letter):
    index = -1
    for i in alphabet:
        index += 1
        if i == letter.upper():
            return index


def index_to_letter(index):
    return alphabet[index]


def vigenere_index(key_letter, plaintext_letter):
    key_index = letter_to_index(key_letter)
    plaintext_index = letter_to_index(plaintext_letter)

    cipher_index = (key_index + plaintext_index) % 26
    return cipher_index

def encrypt_vigenere(key, plaintext):
    cipher_text = ""
    key_index = 0

    for letter in plaintext:
        if letter.isalpha():
            cipher_index = vigenere_index(key[key_index], letter)

            cipher_letter = index_to_letter(cipher_index)

            cipher_text += cipher_letter

            key_index = (key_index + 1) % len(key)
        else:
            cipher_text += letter

    return cipher_text

print(encrypt_vigenere("key", "plaintext"))

def undo_vigenere_index(key_letter, cipher_letter):
    key_index = letter_to_index(key_letter)
    cipher_index = letter_to_index(cipher_letter)
    plaintext_index = (cipher_index - key_index) % 26
    return plaintext_index

def decrypt_vigenere(key, cipher_text):
    plaintext = ""
    key_index = 0

    for letter in cipher_text:
        if letter.isalpha():
            plaintext_index = undo_vigenere_index(key[key_index], letter)
            plaintext_letter = index_to_letter(plaintext_index)
            plaintext += plaintext_letter
            key_index = (key_index + 1) % len(key)
        else:
            plaintext += letter

    return plaintext

print(decrypt_vigenere("key", "ZPYSRROBR"))

encrypted_array = []

def menu():
    menu_options = ["Encrypt", "Decrypt", "Dump Encrypted Text", "Quit"]

    print("Menu Options:")
    for option in menu_options:
        print(option)


    selected_option = input("Type option here: ")

    match selected_option:
        case "Encrypt":
            menu_encrypt()

        case "Decrypt":
            menu_decrypt()

        case "Dump Encrypted Text":
            menu_dump_encrypted_text()

        case "Quit":
            print("Quiting...")

        case _:
            "Invalid option selected, please try again."
            menu()


def menu_encrypt():
    global encrypted_array
    key = input("key: ")
    plaintext = input("plaintext: ")

    encrypted_array.append(encrypt_vigenere(key, plaintext))
    menu()

def menu_decrypt():
    global encrypted_array
    key = input("Enter decryption key: ")
    for encryted_text in encrypted_array:
        print(decrypt_vigenere(key, encryted_text))

    menu()

def menu_dump_encrypted_text():
    global encrypted_array
    for encrypted_text in encrypted_array:
        print(encrypted_text)
    menu()


menu()