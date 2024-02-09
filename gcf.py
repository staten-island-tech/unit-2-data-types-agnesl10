numX = int(input("number 1: "))
numY = int(input("number 2: "))
 
def gcf(numX,numY):
  global gcf
  if numX == 0:
        return numY
  else:
        return gcf (numY, numX % numY)
print("gcf is: ", gcf (numX,numY))
gcf ()