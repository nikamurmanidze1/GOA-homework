def func(str_list,join_char):
    result = ''
    for word in str_list:
        result = result + word + join_char
    return result[0 : -1]

print(func(["html" , "Java" , "Python" , "c++"],"-"))