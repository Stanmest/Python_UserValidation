import string
import random

def User_details():
  first_name = string(input("Enter your first name \n"))
  last_name = string(input("Enter your Last name \n"))
  user_email = input("Enter your email \n")
  details = [first_name,last_name,user_email]
  return details

def User_password():
  characters = string.ascii_letters
  length = 5
  random_pass = ' '.join(random.choice(characters)for i in range(length))
  password = str(details[0][0:2] + dtails[1][-2:] + random_pass)
  return password

status = True
container = []

  while status:
    details = User_details()

    password = User_password(details)
    print("Your password is " + str(password))

    password_like = str(input("Do you like the password? if No, input a new password"))

    password_loop = True

    while password_loop:
      if password_like == "Yes":
        details.append(password)
        container.append(detials)

        password_loop = False;
      else:
        new_password = str(input("Enter a new password longer than 7 "))

        pass_len = True

        while pass_len:
          if len(new_password) >= 7:
            details.append(new_password)

            container.append(details)

            pass_len = False

            password_loop = False

          else:
            print("Your password is less than 7")
            new_password = str(input("Enter a password longer than 7"))
  
  #add new user
  new_user = str(input("Would you like to add a new user? Yes or No"))
  if (new_user == "No"):
    status = False
    for person_details in container:
      print(person_details)
  else:
    status = True
    