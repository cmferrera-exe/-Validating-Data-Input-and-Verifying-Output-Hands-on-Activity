
try:
    age = int(input("Enter your age: "))

    if 12 <= age <= 18:
        print("Valid age.")
    else:
        print("Invalid input. Please enter a whole number.")

except ValueError:
    print("Invalid input. Please enter a whole number.")









