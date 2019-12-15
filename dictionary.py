
name=input("enter name")
address=input("enter address")
location=input("enter location")
origin={'name':name,'address':address,'location':location}
for x in origin.items():
    print(x)