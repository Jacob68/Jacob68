#!/usr/bin/env python
# coding: utf-8

# In[ ]:


user_input = input("Enter (Register)/(Login): ")
def getdetails():
    import re
    regex = r'\b[A-Za-z]+[A-Za-z0-9._%+-]+@[A-Za-z]+\.[A-Z|a-z]{2,}\b'
    while True:
        user_name = input("Enter Your Email ID or Username: ")
        email = False
        if re.fullmatch(regex, user_name):
            email = True
            break
        else:
            print("INVALID")
    if True:
        print("VALID")
    
    import re 
    while True:
        password = input("Enter Your Password : ") 
        pswrd = False 
        if (len(password)<6 or len(password)>16): 
            print("Not Valid !!! Total characters should be between 6 and 16,Please Try Again") 
            continue 
        elif not re.search("[A-Z]",password):
            print("Not Valid !!! It should contain one letter between [A-Z] ,Please Try Again")
            continue 
        elif not re.search("[a-z]",password):
            print("Not Valid !!! It should contain one letter between [a-z] ,Please Try Again") 
            continue
        elif not re.search("[1-9]",password): 
            print("Not Valid !!! It should contain one letter between [1-9] ,Please Try Again") 
            continue 
        elif not re.search("[~!@#$%^&*]",password): 
            print("Not Valid !!! It should contain at least one letter in [~!@#$%^&*] ,Please Try Again") 
            continue 
        elif re.search("[\s]",password): 
            print("Not Valid !!! It should not contain any space ,Please Try Again") 
            continue
        else:
            pswrd = True
            break
    if(True):
        print("Password is Valid")


    with open(f"{user_name}", "w") as f:
        f.write(f"{password}")

def checkdetails():
    user_input = input("ENTER (REGISTER)/(FORGOT PASSWORD): ")
    if user_input == "FORGOT PASSWORD":
        user_name = input("Enter Your Email ID or Username: ")
        try:
            with open(f"{user_name}") as f:
                b = f.read()
                print(b)
        except FileNotFoundError:
            print("Register")
            getdetails()
    if user_input == "Register":
        getdetails()

if user_input == "Register":
    getdetails()

if user_input == "Login":
    user_name = input("Enter Your Email ID or Username: ")
    password = input("Enter Password: ")
    try:
        with open(f"{user_name}") as f:
            a = f.read()
        if a == password:
            print("Valid")
        else:
            print("Invalid")
            checkdetails()
    except FileNotFoundError:
        print("Invalid ,Please Try Again")
        checkdetails()

