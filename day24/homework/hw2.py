# მომხმარებელს შემოტანილი დადებითი მთელი რიცხვი
number = int(input("შემოიტანეთ დადებითი მთელი რიცხვი: "))

# ციკლის გამოყენებით ყველა ამ რიცხვის გამყოფი დამატება სიაში
divisors = [i for i in range(1, number + 1) if number % i == 0]

# დაბეჭდეთ სია
print("gamyofi:", divisors)