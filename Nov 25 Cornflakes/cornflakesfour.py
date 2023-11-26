dogsAgeInHumanYears = int(input("Enter dog's age in Human years: "))
if dogsAgeInHumanYears <= 2:
    age = dogsAgeInHumanYears * 10.5
if dogsAgeInHumanYears > 2:
    age = ((dogsAgeInHumanYears - 2) * 4) + 21
print("The dog's age in dog years is: ", age);