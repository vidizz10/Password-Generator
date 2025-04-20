import random
symbolslettersnumbers = ["!", "?", "+", ".", "-", "_", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
"p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
"M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

def generate_password():
    howmany = int(input("How many characters do you want in your password? "))
    if howmany < 1:
        print("Please enter a number greater than 0.")
        return generate_password()
    elif howmany > 100:
        print("Please enter a number less than 100.")
        return generate_password()
    password = ""
    for i in range(howmany):
        password += random.choice(symbolslettersnumbers)
    return password

print("Your password is: " + generate_password())
print("You can use this password for your accounts.")