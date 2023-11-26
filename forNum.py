total = 0
number = 0

for number in range(20):
	number += 1
	total += number
	number = int(input("Enter number between 1 to 20: "))
print(total, "Is the Total")