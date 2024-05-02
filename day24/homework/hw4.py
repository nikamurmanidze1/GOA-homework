# მთელი რიცხვების სია
numbers = [1, 3, 5, 7, 1, 3, 5, 1, 3,]

# ყველაზე ხშირად განმეორებადი რიცხვის რაოდენობას გამოთვალეთ
most_common_number = max(set(numbers), key=numbers.count)

print("often used:", most_common_number)