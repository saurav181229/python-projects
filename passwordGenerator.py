
import string
import random
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)
password =" "
char = string.ascii_letters+string.digits+string.punctuation
for i in range(15):
    choice = random.choice(char)
    password +=choice
print(password)