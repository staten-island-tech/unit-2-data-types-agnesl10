h = int(input("# of hunger points: "))
a = int(input("# of apples: "))
s = int(input("# of seconds: "))
h = min(h,a)
#the section below is for the constraints that h,a, or s can't be less than 1 or greater than 100000
if (h) < 1 or h > 100000:
    print("hungerpoints error")
if (a) < 1 or a > 100000:
    print("apples error")
if (s) < 1 or s > 100000:
    print("time error")

else:
    if (h-s) < 0:
        print(0)
    else:
        print(h-s)