name = input("pls enter ur name :")
password = input("enter ur password: ")
repeat_paswword = input("pls confirm password: ")

while password != repeat_paswword:
    print("INCORRECT!")
    repeat_paswword = input("try again: ")
else:
    print("correct")