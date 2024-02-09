def all_factors(n):
    factors = []
    for i in range(2,n):
        if n%i == 0:
            factors.append(i)
    return factors
        
number = int(input("enter a number: "))
list_of_factors = all_factors(number)
print(list_of_factors)