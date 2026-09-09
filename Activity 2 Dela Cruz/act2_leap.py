#JOHN BRIAN DELA CRUZ
#BAET 2102
#LEAP YEAR TEST

year = int(input("Enter a year: "))
print((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)