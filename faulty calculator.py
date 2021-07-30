print("THIS IS THE FAULTY CALCULATOR")
s = 0
while (s == 0):
    num1 = float(input("Enter the first number:"))
    num2 = float(input("Enter the second number:"))
    operators = input(
        "Choose the operators among: \n  * (Multiplication)\n  + (Addition)\n  / (Division)\n  - (Subtraction)\n  ** (Square root)\n  ")
    if (num1 == 45 and num2 == 3 and operators == '*'):
        print(num1, "*", num2, "=", "555")
    elif (num1 == 56 and num2 == 9 and operators == '+'):
        print(num1, "+", num2, "=", "77")
    elif (num1 == 56 and num2 == 6 and operators == '/'):
        print(num1, "/", num2, "=", "4")
    elif (operators == "-"):
        print(num1, "-", num2, "=", num1 - num2)
    elif (operators == "**"):
        print(num1, "**", num2, "=", num1 ** num2)
    elif (operators == "%"):
        print(num1, "%", num2, "=", num1 % num2)
    elif (operators == "+"):
        print(num1, "+", num2, "=", (num1) + (num2))
    elif (operators == "*"):
        print(num1, "*", num2, "=", num1 * num2)
    elif (operators == "/"):
        print(num1, "/", num2, "=", num1 / num2)
    else:
        print(" OOPPSS!!!! ,You can choose only the above operations to perform the calculations.")
    option = int(input((" DO YOU WANT TO CONTINUE?(0/1).Press '0' to continue,and '1' to exit : ")))
    if (option == 0):
        continue
    else:
        break
