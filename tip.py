print ("What is your subtotal?")

def subtotal ():
    global subtotal
    subtotal = float(input("< $"))

def tip ():
    global tip
    print ("How was your service?")
    tip = float(input("<"))
    if (input("bad")):
        print ("Sorry, don't pay tip.")
    elif (input("okay")):
        print (f"Pay 15% tip" subtotal * float(0.15)")
    elif (input("good")):
        print (f"Pay 20% tip" subtotal * float(0.20)")
    elif (input("great")):
        print (f"Pay 25% tip" subtotal * float(0.25)")

subtotal ()
tip ()
