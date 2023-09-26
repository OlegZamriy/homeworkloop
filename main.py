початок = int(input("Введіть початок діапазону: "))
кінець = int(input("Введіть кінець діапазону: "))

for число in range(початок, кінець + 1):
    if число % 3 == 0 and число % 5 == 0:
        print("Fizz Buzz")
    elif число % 3 == 0:
        print("Fizz")
    elif число % 5 == 0:
        print("Buzz")
    else:
        print(число)
