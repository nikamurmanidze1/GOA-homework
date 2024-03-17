info_list = []

name =input("pls enter your name: ")
lastname = input("pls enter your lastname: ")
age = int(input("pls enter your age: "))
addres = input("pls enter your living place: ")

info_list.append(name)
info_list.append(lastname)
info_list.append(age)
info_list.append(addres)

print(info_list)
print(info_list[0:2])
print(info_list[1:3])
print(info_list[0:3])
print(info_list[1:3])