print ("Welcome to ATM")
pin = 123
amt = 10000
check = int(input("enter your pin"))
if check == pin:
    print ("your amount is: ", amt)
    wamt = int(input("how much do you want to withdraw: "))
    if wamt > amt:
        print ("you cannot withdraw more than your bank amount")
    else:
        amt = amt - wamt
        print ("you have ", amt ," rupees" )
else:
    print ("wrong pin")
