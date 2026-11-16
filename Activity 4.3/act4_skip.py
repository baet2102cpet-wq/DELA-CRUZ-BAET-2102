#JOHN BRIAN DELA CRUZ
#BAET 2102
#SKIP THE THREES

total = 0

for number in range(1, 51):
    if number % 3 == 0:
        continue

    print(number, end=" ")
    total = total + number

print()
print("Sum:", total)
