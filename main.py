початок = int(input("Введіть початок діапазону: "))
кінець = int(input("Введіть кінець діапазону: "))

кількість_кратних_5 = 0

print("Всі числа в діапазоні:")
for число in range(початок, кінець + 1):
    print(число, end=" ")
print("\n")

print("Всі числа в спадному порядку:")
for число in range(кінець, початок - 1, -1):
    print(число, end=" ")
print("\n")

print("Числа, кратні 7:")
for число in range(початок, кінець + 1):
    if число % 7 == 0:
        print(число, end=" ")
print("\n")

for число in range(початок, кінець + 1):
    if число % 5 == 0:
        кількість_кратних_5 += 1

print("Кількість чисел, кратних 5:", кількість_кратних_5)
