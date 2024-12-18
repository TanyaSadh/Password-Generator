import string
import random
import re


lc=string.ascii_lowercase
up=string.ascii_uppercase
dig=string.digits
sp="!@#$%^&*_-" #providing only those characters which we want in the password generated

pass_count=int(input("Enter the number of passwords you want to generate : "))

password = []
password.extend(lc)
password.extend(up)
password.extend(dig)
password.extend(sp)

def is_easy_password(pwd):
   
    if re.search(r'(0123|1234|2345|3456|4567|5678|6789|abcd|bcde|cdef|defg|efgh|fghi|ghij|hijk|ijkl|jklm|klmn|lmnop|mnopq|nopqr|opqrs|pqrst|qrst|password|name|123|qwerty)', pwd):
        return True  
    
   
    
    return False 


for i in range (pass_count):
    while True:
        pass_length=int(input(f"Enter length of password {i+1} : "))
        if pass_length<=10:
             pwd="".join(random.choices(password,k=pass_length))
             if is_easy_password(pwd):
                print("Password is too easy , generate a stronger password.")
             else:
                print(f"Password {i + 1}: {pwd}")
                break
        else:
           print("Password length must not exceed 10")


"""3 modules used : random , string , re

validations: length of password cannot exceed 10

frequent easy passwords cannot be generated here due to the validation put

join concatenates all the individual characters with "" 


lc , up , dig and sp contain all the possible characters

re.search checks if a pattern is present or not

random.choices can repeat a single character multiple times in the password , it selects that many characters which are given as length in the parameter of that function


"""
             
                   
        




