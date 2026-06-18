# Caesar Cipher

def cipher(text, shift, mode):
    result = ""

    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97

            if mode == "encrypt":
                result += chr((ord(char) - base + shift) % 26 + base)
            else:
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char

    return result


# MAIN
print("🔐 Cipher Tool")

while True:
    print("\n1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "3":
        break

    text = input("Enter text: ")
    shift = int(input("Enter shift: "))

    if choice == "1":
        print("Encrypted:", cipher(text, shift, "encrypt"))

    elif choice == "2":
        print("Decrypted:", cipher(text, shift, "decrypt"))

    else:
        print("Invalid choice")