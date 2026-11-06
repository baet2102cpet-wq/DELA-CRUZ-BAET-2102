#JOHN BRIAN DELA CRUZ
#BAET 2102
#CHANGE CALCULATOR

amount = int(input("Enter amount in pesos: "))
print("100 pesos:", amount // 100)
amount = amount % 100
print("20 pesos:", amount // 20)
amount = amount % 20
print("5 pesos:", amount // 5)
amount = amount % 5
print("1 peso:", amount // 1)