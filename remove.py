list=[2,1,3,5,6,2,2,7,3]
a=int(input("enter the number yow want to remove"))
for x in list:
    if a==x:
      while(list.count(a)):
        list.remove(a)
print(list)

