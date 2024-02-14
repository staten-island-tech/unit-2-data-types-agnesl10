x = int(input("number 1: "))
y = int(input("number 2: "))
factors = []
def gcf(x,y):
  for i in range(2,y):
      if x%i == 0 and y%i == 0:
            factors.append(i)
gcf(x,y)#REMEMBER TO RUN FUNCTION
print("gcf is: ", factors[-1])

#SAVE BEFORE YOU RUN