number = int(input("Enter a number: "))

count = 1

while count <= 10:
    product = number * count
    print(number, "x", count, "=", product)
    count = count + 1