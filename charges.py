num =int(input("Enter number of units used: "))

if num < 100 :
	print("0 charges")


elif (num > 100 and num < 200):
	charges = ((num-100) * 10)
	print (charges)
elif (num > 200):
	charges = (((num-200)* 20) + 1000)
	#charges = ((num % 100) * 20) + ((((num // 100) * 100)-100) * 10)
	print (charges)


else:
	print("try again")
