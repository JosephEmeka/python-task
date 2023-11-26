for number in range(2, 101): 
    for num in range(2, 101):
        if number % num == 0:
            break
    if number == num:
        print(number,end=",")