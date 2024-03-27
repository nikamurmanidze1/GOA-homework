def aritmetikuli(num_list):
    sum = 0
    for i in num_list:
        sum += i
    mean = sum / len(num_list)
    print(mean)
lst = [1,2,3,4,5]
aritmetikuli(lst)