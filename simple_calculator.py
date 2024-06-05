print(" --- SIMPLE CALCULATOR ---")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Press 1 for addition \nPress 2 for subtraction \nPress 3 for multiplication \nPress 4 for division")

choice = int(input("Enter your choice from 1 to 4: "))

if choice == 1:
    print("Addition of given two numbers is", num1+num2)
elif choice == 2:
    print("Subtraction of given two numbers is", num1-num2)
elif choice == 3:
    print("multiplication of given two numbers is", num1*num2)
elif choice == 4:
    print("Division of given two numbers is", num1/num2)
else:
    print("Invalid choice")
