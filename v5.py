#can't figure out the placement of the variable Strong#

#Creating Yes and no list
yesList = ["Yes", "Y", "y", "Yeah", "yes"]
noList = ["No", "N", "n", "Nah", "no"]

#importing regular expressions to help determine the types of characters in the password
import re 

#Asking the user to create and enter a suitable password
print ("Please choose a suitable password.")
passone = input(str("Enter your chosen password: "))
def enterpass():
  
#Creating a function to check whether the password re-entered matches the first one
  passtwo = input(str("To confirm, type the password again: ")) 
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

def password(passone):

  if len(passone) <=8:
    print("Your password must be 8 characters long.")
    return False
  elif not re.findall(r'\d+', passone):
    print("You need a number in your password.")
    return False
  elif not re.findall(r'[A-Z]+', passone):
    print("You need a capital letter in your password.")
    return False     
  elif not re.findall(r'[£$%^&*@]', passone):
    print("You need a symbol in your password.")
    return False
  else:
    print("Password Accepted")
    return True


def passstrong():
    a = '[A-Z]'
 
    b = '[£,$,%,^,&,*,@]'
 
    c = '\d+'
 
    d = '[a-z]'
 
    if password(passone) == a and b and c and d:
      print("Very Strong Password")
        
    if password(passone) == a and b and c or b and c and d or a and c and d:
      print("Strong Password")
 
    if password(passone) == a and b or a and c or a and d or b and d or c and d:
      print ("Medium Password.")
 
    if password(passone) == a or b or c or d:
      print ("Weak Password.") 

enterpass()
password(passone)
passstrong()

