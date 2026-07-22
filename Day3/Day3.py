#Ladder if elif else

Signal=input("Enter the Signal Colour:")

if Signal == "Red" :
    print("Stop")
elif Signal == "Yellow":
    print("Ready")
elif Signal == "Green":
    print("Go")
else:
    print("Invalid SignalColour")

#Nested if else

Balance=5000

Pin=int(input("Enter the Atm Pin:" ))

if Pin==1234 :
    Amount=int(input("Enter The Amnount:"))
    if Amount<=Balance :
        print("Withdrawal Successfully")
    else :
        print("Insufficent Balance")
else :
    print("Invalid Pin")
    
#Match Case

BusNumber=int(input("Enter the Bus Number"))

match BusNumber :
    case 17 :
        print("Island Grounds")
    case 27 :
        print("Villivakkam")
    case 25 :
        print("Anna Square")
    case 26 :
        print("Royapuram")
    case 5 :
        print("Besant Nagar")
    case _:
        print("There are no bus in this number ")



        
