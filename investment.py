

principal = int(input("Enter principal(original amount invested): "))
annualReturnRate = int(input("Enter annual rate of return: "))
numberOfYears = int(input("Enter number of years (10, 20 or 30)   : "))
amountAtNthYear =  principal * ((1 + annualReturnRate) ** numberOfYears)
print(amountAtNthYear)