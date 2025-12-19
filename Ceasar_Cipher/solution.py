alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g',
    'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u',
    'v', 'w', 'x', 'y', 'z'
]
def encrypt(original_text , shift_amont):
    cipher = ""
    for letter in original_text:
        if letter in alphabet:
            shifed_position = (alphabet.index(letter)+shift_amont)%26
            cipher+=alphabet[shifed_position]
        else:
            cipher += letter
    print(f"Here is encrypted text: {cipher}")


def decrypt(encrypted_text , shift_amont):
    cipher = ""
    for letter in encrypted_text:
        if letter in alphabet:
            shift_position =(alphabet.index(letter)-shift_amont)%26
            cipher+=alphabet[shift_position]
        else:
            cipher+=letter
    print(f"Here is decrypted text: {cipher}")
while True:
    direction = input("Do you want encrypt or decrypt?: ")
    text = input("Enter your text: ")
    shift = int(input("Enter your shift: "))
    if direction == "encrypt":
        encrypt(text,shift)
    elif direction == "decrypt":
        decrypt(text,shift)
    else:
        print("Invalid input")

    output = input("Do you want to try again? (yes/no): ").lower()
    if output != "yes":
        print("You finished.")
        break



