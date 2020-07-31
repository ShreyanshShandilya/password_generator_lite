import string
import random
lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
digits = list(string.digits)
punctuations = list(string.punctuation)
All = lower + upper + digits + punctuations

def password(length = 15):
    passw = ""
    for _ in range(length):
        passw = passw + random.choice(All)
    return passw

try:
    length = int(input("Enter the length of password you want to generate "))
    if (length <= 0):
        print("Invalid Length")
    else:
        s = password(length)
        print((s))
except:
    print("Invalid input")
