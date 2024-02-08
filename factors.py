def all_factors(f):
    factors = []
    for i in range(1,f+1):
        if f%i == 0:
            factors.append(i)

number = int(input("enter a number: "))
list_of_factors = all_factors(number)
print(list_of_factors)