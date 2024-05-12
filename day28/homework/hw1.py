def multiples_3_or_5(num):
    if num < 0:
        return 0
    
    multiple_sum = 0
    for i in range(num):
        if i % 3 == 0 or i % 5 == 0:
            multiple_sum += i
    return multiple_sum


print(multiples_3_or_5(10))  #23
