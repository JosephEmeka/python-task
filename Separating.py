integer = int(input("Enter five integers: "))

digit5 = integer % 10 
digit4 = (integer % 100) // 10
digit3 = (integer % 1000) // 100
digit2 = (integer % 10000) // 1000
digit1 = (integer % 100000)//  10000

print(digit1,"	", digit2, "	", digit3, "	", digit4,"	", digit5)

