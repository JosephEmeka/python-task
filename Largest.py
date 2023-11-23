firstInteger = int(input("Enter first integer: "))
secondInteger = int(input("Enter second integer: "))
thirdInteger = int(input("Enter third integer: "))

sum = firstInteger + secondInteger + thirdInteger


average = sum / 3

product = firstInteger * secondInteger * thirdInteger

print(sum, average, product)

if (firstInteger < secondInteger) and (firstInteger < thirdInteger):
	print (firstInteger, "is the smallest")

elif (secondInteger < firstInteger) and (secondInteger < thirdInteger):
	print (secondInteger, "is the smallest")


else:
	print (thirdInteger, "is the smallest")


if (firstInteger > secondInteger) and (firstInteger > thirdInteger):
	print (firstInteger, "is the largest")

elif (secondInteger > firstInteger) and (secondInteger > thirdInteger):
	print (secondInteger, "is the largest")


else:
	print (thirdInteger, "is the largest")