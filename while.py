import sys
name=input("enter your name")
for x in range(1,4):
    if name.isalpha()==True and len (name)>3:
        print("name authenication done")
        break
    else:
        print ("wrong input")
        name=input('enter again')
sys.exit()

print("{now for age verification}")

age=int(input("enter your age"))
for x in range(1,4):
    if age.isdigit()==True and len(age)>=18:
        print("age authenication done")
        break
    else:
        print("wrong input")
        age=int(input("enter again")
print("now for mobileno verification")