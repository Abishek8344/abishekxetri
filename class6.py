'''def area (r):


    Area=3.14*r*r
    return Area


rad=float(input('enter the val of radius'))
area=area(rad)
print("the area of circle is",area)'''

'''def sum(a,b):
    sum=a+b
    return sum


x=int(input("enter the first number"))
y=int(input("enter the second number"))
z=sum(x,y)
print("the sum is",z)'''

'''def sub(a,b):
    sub=a-b
    return sub

x=int(input("enter first number"))
y=int(input("enter second number"))
z=sub(x,y)
print("the difference is",z)'''


'''def power(a,b):
    pow=a**b
    return pow
x=int(input("enter the first one"))
y=int(input("enter the second one"))
z=power(x,y)
print("the power is",z)'''

'''def arm(a):
    order=len(str(a))
    sum=0
    while a>0:
        num=a%10
        sum=sum+num**order
        a=a//10
    return sum
num1=int(input("enter any number"))
sum1=arm(num1)
if sum1==num1:
    print("armstrong")
else:
    print("not armstrong")'''


'''#palindrome
def pal(n):
    rev=0
    while n>0:
        num=n%10
        rev=rev*10+num
        n=n//10
    return rev
num1=int(input("give me an input"))
sum=pal(num1)
if sum==num1:
    print("palindrome")
else:
    print("not palindrome")'''

#factorial
def fact(n):
    while n>0:
        fact=n*(n-1)
    return fact
num1=int(input("enter the number"))
factorial=fact(num1)
    print("the factorial is",factorial)















