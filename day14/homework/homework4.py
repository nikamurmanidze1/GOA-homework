def numbers(num):
    num1 = 0
    num2 = 0
    for i in num:
        if i > 0:
            num1 += i
        elif i < 0:
            num2 += i
    print(num1)
    print(num2)
numb = [1,-1,2,-2,3,-3]
numbers(numb)