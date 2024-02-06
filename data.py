""" #Data types, numbers 1,2,3
def add(x,y):
    print(x + y)
add(45,35)

#strings "a,b,c"
def message(name):
    print(name)
message("Agnes")
x="1"
int(x)
add("35","45")

#booleans
x = True

def check(x):
    if(x == True):
        print("is logged in")
    else: 
        print("please login")
check(x) """

values = [1,2.23,5,7,2,30,15]
print(values)
for i in values:
    print(values[0]) #brackets show position in list.


#strings
x = "this is a thing"
y= x.split( ) #splits with space : ['this', 'is', 'a', 'thing']
z = y[0] #specific location in list above ^^
print(y)
print(z)

even_or_odd = int(input("integer"))
if (even_or_odd) == 0:
    print("even")
else:
    print("odd") 
