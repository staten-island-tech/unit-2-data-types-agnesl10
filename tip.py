print ("What is your subtotal?")

def subtotal ():
    global subtotal
    subtotal = float(input("< $"))

def tip ():
    global tip
    print ("How was your service?")
    tip = (input("<"))
    if ((tip) == "bad"):
        print (f"Sorry, don't pay tip.")
    elif ((tip) == "okay"):
        print (f"Pay 15% tip {subtotal * float(0.15)}")
    elif ((tip) == "good"):
        print (f"Pay 20% tip {subtotal * float(0.20)}")
    elif ((tip) == "great"):
        print (f"Pay 25% tip {subtotal * float(0.25)}")

subtotal ()
tip ()
