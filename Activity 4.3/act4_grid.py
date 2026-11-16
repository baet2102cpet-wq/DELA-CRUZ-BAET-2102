#JOHN BRIAN DELA CRUZ
#BAET 2102
#MULTIPLICATION GRID

while True:
    try:
        size = int(input("Size: "))
        if 1 <= size <= 10:
            break
        print("Please enter a size from 1 to 10.")
    except ValueError:
        print("Invalid input. Please enter an integer from 1 to 10.")

for row in range(1, size + 1):
    for column in range(1, size + 1):
        print(format(row * column, "4d"), end="")
    print()
