import random 
number = random.choice([1,2,3,4,5,6,7,8,9,10])
(x) = int(input("Guess: "))
while (x) != number:
    if x < number:
        print("try again; it's greater")
     
    elif x > number:
        print("try again; its smaller")
    
    int(input("guess again: "))  
else:
    print("correct")
