word = input("Please enter uppercase word: ")

result = ''

for index in range(len(word)):
    if index % 2 == 0:
        result = result + word[index].upper()
    else:
        result = result + word[index].lower()

print(result)