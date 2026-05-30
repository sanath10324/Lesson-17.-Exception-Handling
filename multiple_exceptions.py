try:
    num1, num2 = eval(input("Please enter two numbers, separated by a coma: "))
    result = num1 / num2
    print("Result is", result)

except ZeroDivisionError:
    print("Division by zero is error !!")

except SyntaxError:
    print("Comma is missing, enter comma seperated like this 1,2 !")

except:
    print("Wrong Input")

else:
    print("No Exceptions")

finally:
    print("This will excecute no matter what!!")
    