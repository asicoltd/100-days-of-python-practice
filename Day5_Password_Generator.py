import random
alphabetList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numberList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbolList = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']

length = int(input("How many letter in the password do you want:"))
numbers = int(input("How many number:"))
characters = int(input("How many character:"))
length = length - numbers - characters
password = [alphabetList[random.randint(0,52)]]

for i in range(0,length):
    password += alphabetList[random.randint(0,53)]
    passwordMain += passwordMain + password[i]

