
name=str(input("enter your name"))
#validating
if  name.isalpha()==True and len(name)<=5 or ' ' in  name:
        print("it is invalid")
else:
        print("it is invalid")


age=input("enter your age")
if age.isdigit()==True and int(age)>=18:
        print("permitted")
else:
        print("restricted")
phonenum=input("enter your phonenumber")
if phonenum.isdigit()==True and len(phonenum)>=10:
        print ("valid")
else:
        print("invalid")