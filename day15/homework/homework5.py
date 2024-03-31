def calculator(operation,num1,num2):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 != 0:
            return num1 / num2
        else:
            return"Error"
    else:
        return"Error"

print(calculator("add", 1,5))
    

    