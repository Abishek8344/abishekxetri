'''f=open("hello.txt","w")
f.writelines("wake me up when semptember ends")
f.close()

#code to replace the contents of files
with open("hello.txt") as f:
    with open("copy.txt", "w") as f1:
        for line in f:
            f1.write(line)'''

'''f=open("our.txt","r+")
f.writelines("hello-this-is-a-text-file")
text1=f.read()
print(text1)
text2=text1.replace("-"," ")
print(text2)
f.close()'''

#code to update file at particular location

'''f=open("whiplash.txt","w")
f.writelines("let the music flows")
f.close()
n_text=input("wha do you want to add/update")
loc=int(input("enter the location"))
f1=open("whiplash.txt","r")
old_text=f1.readline()
print(old_text)
f1.seek(loc)
new_text=old_text[:loc]+n_text+old_text[loc:]
print(new_text)
f1.close()

f2=open("whiplash.txt","w")
f2.writelines(new_text)
f2.close()'''














#prime numbers using list comprenhision
'''prime_num=[x for x in range(1,2500) if all (x%y!=0 for y in range(2,x))]
print(prime_num)'''


'''def cube(n):
    return n**3
list1=[2,4,5,6]
list_n=list(map(cube,list1))
print(list_n)'''

'''def square(a):
    return a**2
num=[2,4,6,8]
output=list(map(square,num))
print(output)'''


'''#error handling
age=int(input("enter any age")
    if age <18:
        raise Age error
    else:
        print("accepted")'''

'''class StringLenError(exception):
    def_init_(self):
    super(StringLenError,self)_init_("string should be grater than 3")
    age=str(input("enter the string"))
if str<3:
        raise StringLenError
else:
    print("accepted")'''














