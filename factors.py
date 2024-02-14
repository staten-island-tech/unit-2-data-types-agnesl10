def all_factors(n):
    factors = []
    for i in range(2,n): #starts at 2 then continues. thought i was 0 so you have to start at 2 b/c 45%0 breaks down the code.
        if n%i == 0:
            factors.append(i)
    return factors #return ends the code so you have to put it in the function w/o
        
number = int(input("enter a number: "))
list_of_factors = all_factors(number)
print(list_of_factors)