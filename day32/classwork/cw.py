def count_vowels(input_string):
    xmovnebi = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0
    for i in input_string:
        if i in xmovnebi:
            vowel_count += 1
    return vowel_count

input_string = "goaaaaaaa"
print(count_vowels(input_string))  











def square_digits(num):

    num_str = str(num)
    result = ""
    for digit in num_str:
        squared_digit = str(int(digit) ** 2)
        result += squared_digit
    return int(result)


print(square_digits(2939))  # Output: 811181
print(square_digits(765))   # Output: 493625