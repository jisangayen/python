
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Divide")


choice = int(input("Enter Your choice: "))

if choice<=4:
    print("Yes")
else:
    print("break")
    




num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == 1:
    print(num1, "+", num2, "=", num1+num2)

elif choice == 2:
    print(num1, "-", num2, "=", num1-num2)
elif choice == 3:
    print(num1, "*", num2, "=", num1*num2)
elif choice == 4:
    print(num1, "/", num2, "=", num1/num2)
else:
    print("Invalid syntax, Try again")
