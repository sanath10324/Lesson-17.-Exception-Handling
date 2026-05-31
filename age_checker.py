try:
    age = int(input("Please enter your age: "))

    if age %2 == 0:
        print("Your age is an even number!")
    else:
        print("Your age is an odd number!")

except ValueError:
    print("VALUE ERROR !!, Please enter a whole number age!!")