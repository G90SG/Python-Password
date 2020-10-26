#attempting to take out the functions to see if that helps#
#Creating Yes and no list
yesList = ["Yes", "Y", "y", "Yeah", "yes"]
noList = ["No", "N", "n", "Nah", "no"]

#importing regular expressions to help determine the types of characters in the password
import re 

#Asking the user to create and enter a suitable password
print ("Please choose a suitable password.")

passone = input(str("Enter your chosen password: "))
#Creating a function to check whether the password re-entered matches the first one

passtwo = input(str("To confirm, type the password again: ")) 
# Checking whether passwords match
if passone == passtwo:
  print("Great, your passwords match.")
else:
  print("Your passwords don't match.")
  again = input("Would you like to try again? ")
  if again in yesList:
   passtwo = input(str("To confirm, type the password again: ")) 
  elif again in noList:
    print ("Goodbye. ")
  else:
    print ("That's not the answer I was looking for, Goodbye. ")


strong = 5  
while strong > 0:
  if (len(passone )>8):
    strong = strong-1 
  if re.search("[a-z]", passone):
    strong = strong-1 
  if re.search("[A-Z]", passone):
    strong = strong-1
  if re.search("[0-9]", passone):
    strong = strong-1 
  if re.search("[£$%^&*@]", passone):
    strong = strong-1
  else:
    print("Your password is not suitable.")


if strong == 0:
  print("Your password is very strong.")
elif strong == 1:
  print("Your password is strong.")
elif strong == 2: 
  print("Your password is moderately strong.")
elif strong == 3:
  print("Your password is fine")
elif strong == 4:
  print("Your password is weak.")
elif strong == 5:
  print("Your password is very weak.")
else:
  print("n")




