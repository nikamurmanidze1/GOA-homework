def multiply(a, b):
    return a * b

def litres(time):
    return time // 2

def grow(arr):
    smth = 1
    for i in arr:
        smth *= i
    return smth

def fake_bin(x):
    y = ''
    for i in x:
        if int(i) < 5:
            y += '0'
        else:
            y += '1'
    return y

def to_jaden_case(string):
    list  = string.split()
    new_list = [i.capitalize() for i in list]
    print(new_list)
    return " ".join(new_list)


def accum(st):
    return '-'.join([(l * i).title() for i, l in enumerate(st ,1)])

def remove_smallest(numbers):
    if len(numbers) == 0:
        return []
    minimum = min(numbers)
    working_numbers = numbers.copy()
    working_numbers.remove(minimum)
    return working_numbers

def solution(number):
    sum = 0
    for i in range(1,number):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum