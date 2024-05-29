def square_digits(num):
    num_str = str(num) 
    squared_digits = []

    for char in num_str:
        digit = int(char)
        squared_str = str(digit ** 2)
        squared_digits.append(squared_str)
    concatenated_result = ''.join(squared_digits)
    result = int(concatenated_result)
    
    return result


print(square_digits(456))   