import random
import string

def ask_types():
    include_uppercase = input("Do you want to include uppercase letters?(Y/N):").strip().upper() == "Y"
    include_lowercase = input("Do you want to include lowercase letters?(Y/N):").strip().upper() == "Y"
    include_numbers = input("Do you want to include numbers?(Y/N):").strip().upper() == "Y"
    include_symbols = input("Do you want to include symbols?(Y/N):").strip().upper() == "Y"
    return include_uppercase,include_lowercase,include_numbers,include_symbols
def main():
    password_length = int(input("How long is your password?"))
    
    uppercase,lowercase,numbers,symbols = ask_types()

    possible_characters = ""
    if uppercase:
        possible_characters += string.ascii_uppercase
    if lowercase:
        possible_characters += string.ascii_lowercase
    if numbers:
        possible_characters += string.digits
    if symbols:
        possible_characters += string.punctuation

    if not possible_characters:
        print("You need to include at least one type of character")
        return

    password = ""
    for i in range(password_length):
        password+=random.choice(possible_characters)

    print(password)

if __name__=="__main__":
    main()