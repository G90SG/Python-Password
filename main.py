#first draft saved#
#Creating Yes and no list
yesList = ["Yes", "Y", "y", "Yeah", "yes"]
noList = ["No", "N", "n", "Nah", "no"]

#Asking the user to create and enter a suitable password
print ("Please choose a suitable password.")
passone = input ("Enter your chosen password: ") 

#Creating a function to check whether the password re-entered matches the first one
def password():
  passtwo = input ("To confirm, type the password again: ") 

# Checking whether passwords match
  if passone == passtwo:
    print("Great, your passwords match.")
    validation(passone)
  else:
    print("Your passwords don't match.")
    again = input("Would you like to try again? ")
    if again in yesList:
      password()
    elif again in noList:
      print ("Goodbye. ")
    else:
      print ("That's not the answer I was looking for, Goodbye. ")

def validation(passone):

  

password()
validation(passone)