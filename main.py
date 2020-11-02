#Create a program that asks the user to input a password, re-enter the password
#and then tells the user if the password is weak, medium or strong.
passone = input("Enter a password here: ")

weak = "This password is weak, consider adding some extra characters, upper letters or numbers!"
medium = "This password is medium, consider adding some numbers to make it stronger!"
strong = "This password is is considered strong!"
#Make sure the password is ok
if len(passone) > 12:
    print("Your password must be longer than 5 and below 12!")
elif len(passone) < 6:
    print("Your password must longer than 5 and below 12!")
lowercase_found = 0
uppercase_found = 0
numeric_found = 0
#Set flags where appropriate
for ch in passone:
    if ch.islower():
        lowercase_found = 1
    if ch.isupper():
        uppercase_found = 1
    if ch.isdigit():
        numeric_found = 1
#Exit if all flags have been set
    if lowercase_found and uppercase_found and numeric_found:
        break
#Calculate password strength and print results
password_strength = lowercase_found + uppercase_found + numeric_found
#If password meets all three critertias
if password_strength in range (1,4):
    print("The password", passone, "is valid.")
#Print out password strength
    if password_strength == 1:
        print("Password", passone, "is a WEAK password!")
    elif password_strength == 2:
        print("Password", passone, "is a MEDIUM password!")
    else:
        print("Password", passone, "is a STRONG password!")
else:
    print("Invalid password: ", passone, "contained neither letters or numbers!")