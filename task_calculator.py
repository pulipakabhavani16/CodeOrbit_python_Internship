# CodeOrbit Internship - Task 1
# Simple Calculator

print("===== SIMPLE CALCULATOR =====")

try:
    # Taking input from the user
    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))

    # Display menu
    print("\nChoose an Operation")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter your choice (1/2/3/4): ")

    # Perform operation
    if choice == "1":
        result = num1 + num2
        print("Result =", result)

    elif choice == "2":
        result = num1 - num2
        print("Result =", result)

    elif choice == "3":
        result = num1 * num2
        print("Result =", result)

    elif choice == "4":
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print("Result =", result)

    else:
        print("Invalid Choice!")

except ValueError:
    print("Please enter valid numbers.")

except Exception as e:
    print("Error:", e)

print("\nThank you for using the Simple Calculator!")