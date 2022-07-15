
a= int (input("Enter First side of triangle: " ))
b= int (input("Enter second side of triangle:" ))
c= int (input("Enter Third side of triangle: " ))

s= (a+b+c)/2

area= (s*(s-a)*(s-b)*(s-c))**0.5

print("The area of trangle", area)