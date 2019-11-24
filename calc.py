'''mini calculator project with some simple features'''
name=str(input("enter your name"))
password=str(input("enter your password"))

if name.isalpha()==True and len(name)>=5:
    print("it is valid")
else:
    print("it is invalid")

if password.isalpha()==True and len(password)>=5:
    print("it is valid")
else:
    print("it is invalid")
print("A.Basic calculator")
print("B. calculator with some extra features")
input1=input("select the type of calculator you want to use")
if input1=='A':
   print("select the type of the operation you want to use")
   print("1.Addition")
   print("2.Subtract")
   print("3.Multiply")
   print("4.Divison")


   # Take input from the user
   choice = input("Enter choice(1/2/3/4): ")

   #num1 = float(input("Enter first number: "))
   #num2 = float(input("Enter second number: "))

   if choice == '1':
         print("\tFor Addition operation: \n")
         num1 = float(input("\tEnter the first number..   "))
         num2= float(input("\tEnter the second number..  "))
         add = float(num1 + num2)
         print("\t", num1, "+", num2, "=",add)
   elif choice == '2':
         print("\tFor Subtraction operation: \n")
         num1 = float(input("\tEnter the first one..   "))
         num2 = float(input("\tEnter the second one..  "))
         subtract = float(num1 - num2)
         print("\t", num1, "-", num2, "=", subtract)
   elif choice == '4':
         print("\tFor Division operation: \n")
         num1 = float(input("\tEnter the first one..   "))
         num2 = float(input("\tEnter the second one..  "))
         division = float(num1 / num2)
         print("\t", num1, "/", num2, "=", division)
   elif choice == '3':
         print("\tFor Multiplication operation: \n")
         num1 = float(input("\tEnter the first one..   "))
         num2 = float(input("\tEnter the second one..  "))
         multiply = float(num1 * num2)
         print("\t", num1, "*", num2, "=", multiply)
   else:
         print("input the operation again")


elif input1 == 'B':
    print("select the operation")
    print("1.simple interest")
    print("2.temperature conversion")






