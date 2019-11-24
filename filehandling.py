'''f=open('file.txt','w')
f.writelines("my name is ")
f.close()





with open("file.txt","r") as f:
    text = f.read()
    print(text)

f=open("file.txt","a")
f.writelines("\tabishek")
f.close()
with open("file.txt","r") as f:
    text=f.read()
    print(text)'''


'''#user defined wala
f1=open("file2.txt", "w")
text=input("write to file, write shit to stop")
while text!="shit":
    f1.writelines(text+ '\n')
    text=input()
print("done with all this stuff")
f1.close()'''


