word = input("enter random word: ")
for i in word:
    if word == word.lower():
        input("try again: ")
    if word != word.lower():
        print("Correct!")