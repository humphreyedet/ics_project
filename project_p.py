import math
import string
import random

alphabets = list(string.ascii_letters) # Declare a list of string alphabets
digits = list(string.digits) # Declare a list of string numbers
specialC = list("@#$=+-%*") # Declare a list of string special characters(Symbols)

counter = 0 # global variable declaration

def passwordGenerator(): #Begin Password Function
    global counter # references global variable *counter*

    specialC_count = digits_counts = alphabets_count = 0 # local variable declaration

    password = [] # declare an array called password

    if counter == 0: # checks if this message has already been displayed once: if counter is 0 then display else don't
        intro_message()
   
    length = int(input("Input Password Length: ")) # Input Password Length

    permittedPasswordLength(length) # Check if password length is allowed 

    rest_modulo = length%3 # get the rest value when actuall value is divided by 3
    rest_division = math.floor(length/3) # get the whole number when a value is divided by 3
    
    if  (length >6 and rest_modulo ==1) and rest_division >=2: # captures all length values which >6 & when divided by 3 produces a rest value of 1 :(7,10,13,16,19...)
        alphabets_count = rest_division +1
        digits_counts = rest_division
        specialC_count = rest_division
    elif (length >6 and rest_modulo ==2) and rest_division >=2: # captures all length values which >6 & when divided by 3 produces a rest value of 2 :(8,11,14,17,20...)
        alphabets_count = rest_division +1
        digits_counts = rest_division +1
        specialC_count = rest_division
    
    if length >=6 and rest_modulo ==0 and rest_division >=2: # captures all length values which are >=6 & when divided by 3 produces a wholenumber that is >=2, with a rest value 0 :(6,9,12,15,18)
        alphabets_count = rest_division
        digits_counts = rest_division
        specialC_count = rest_division

    for i in range(alphabets_count):
        password.append(random.choice(alphabets)) # genrate a radom ascii string of the given alphabets_count length and add it into the password array

    for i in range(digits_counts):
        password.append(random.choice(digits)) # genrate a radom digit string of the given digits_counts length and add it into the password array

    for i in range(specialC_count):
        password.append(random.choice(specialC)) # genrate a radom special character string of the given specialC_count length and add it into the password array

    random.shuffle(password) # mix the password array indexes together
    print("".join(password)) # join all the values in the array indexes together to create a single string
    quit() # Exits the programm
    
def permittedPasswordLength(length):  # if length < 6 then go back to the begining
    if length < 6:
        print("Minimum password length is 6")
        passwordGenerator()
    return # if lenght is >= 6 then continue

def intro_message():
    global counter # references global variable "counter"
    print("Welcome to Rahul_group Password Generator!!")
    username = input("Enter username:")
    groupname = input("Enter groupname:")
    print("Hello",username,"this Password Generator project was done by",groupname)
    counter = counter+1 # Increment counter by one after this code block have been executed

passwordGenerator() # starts the password generator