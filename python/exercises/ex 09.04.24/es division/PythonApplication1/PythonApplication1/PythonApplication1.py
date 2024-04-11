num = int(input("enter a num "))
x1 = num % 10
num = num // 10
x2 = num % 10
num = num // 10
x3 = num
sumOfStones = x1+x2+x3
print("The number of stones collected by all the pigs is:", sumOfStones)
print("If they divide the stones equally, each will get:", sumOfStones // 3)
print("The remainder of the division of the stones is:", sumOfStones % 3)
print((sumOfStones % 3) == False)
