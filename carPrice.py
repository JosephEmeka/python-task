carPrice = int(input("Enter Price of Car: "))

if carPrice < 1000000:
	print(0.1 * carPrice)
	 

elif carPrice >= 1000000 and carPrice < 3000000:
	print(0.15 * carPrice)
	

elif carPrice >= 3000000 and carPrice < 5000000:
	print(0.2 * carPrice)
		
	
elif carPrice >=5000000:
	print(0.25 * carPrice)
		
