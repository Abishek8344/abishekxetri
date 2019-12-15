dic={}
a='yes'
while a=='yes':
    key=input("enter some key")
    value=input("enter your value of key")
    if value.isdigit()==True:
        value=int(value)
    else:
        value=str(value)
        #inserting entered key and value to the dictionary
        dic[key]=value

        a=input('type yes for more adding')
        print(dic)