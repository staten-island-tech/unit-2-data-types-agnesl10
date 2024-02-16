import random 
(x) = int(input("Guess: "))
number = random.choice([1,2,3,4,5,6,7,8,9,10])
while (x) != number:
    if x < number:
        print("try again; it's greater")
    if x > number:
        print("try again; its smaller")
    
    int(input("guess again: "))  
else:
    print("correct")
