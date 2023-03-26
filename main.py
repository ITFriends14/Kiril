print("name: ", input("Напишіть ім'я: "))

num1 = 1 # int
num2 = 1.9 # int
print(type(num1 + num2)) # float

print(1 + int("2"))
print(True, False) # bool

print(num1 == 1, num2 != 1.9) # 1: True, 2: False

notbox = (1, 2, 3, 4, 5, 6, 7)

print(notbox)
print(notbox[0]) # 1 елемент
print(notbox[6]) # 2 елемент

box = [10, 19, 7, 5, 8] # list

box[0] = 1
print(box)

country = ["Молдова", "Ватикан", "Північна македонія", "Катар", "Непал"]
print(country[2], country[4])

country[1] = "Аргентина"
country[4] = "Португалия"