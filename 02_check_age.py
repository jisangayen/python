
# Take input of age of 3 people by user and determine oldest and youngest among them.

age1 = int(input("Enter Your age: "))

age2 = int(input("Enter Your age: "))

age3 = int(input("Enter Your age: "))


if age1>age2 and age1>age3 :
    print("Age 1 You are Elder")

if age2>age3 and age2>age1:
    print("Age 2 You are Elder")    

if age3>age2 and age3>age1:
    print("Age 3 You are Elder")  

if age1<age2 and age1<age3 :
    print("Age 1 You are Younger")

if age2<age3 and age2<age1:
    print("Age 2 You are Younger")    

if age3<age2 and age3<age1:
    print("Age 3 You are Younger")      