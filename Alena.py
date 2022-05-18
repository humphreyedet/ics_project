#import module random
import random
#create a function pass_gen
def pass_gen(length):
  digits='1234567890'
  letter='ABCDEFGHIJKLMNOPRSTUVWXYZabcdefghijklmnoprstuvwxyz'
  symbol='!@#$%^&*()_+'
  password=''
 
 #password generation
  if length<12:
    return print ('Error! password shoud be more then 12 symbols')
  else:
    password+=random.choice(digits)
    password+=random.choice(letter)
    password+=random.choice(symbol)
    while len(password) < length:
      password+=str(random.choice([random.randint(0,3)]))

    password_list = list(password)  
    random.shuffle(password_list)
    print("".join(password_list))
    # print(password)

pass_gen(12)
      