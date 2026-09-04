balance = 20000
while True:
    option =int(input("enter option\n 1-DEPOSIT MONEY\n 2-WITHDRAW MONEY\n 3-CHECK BALANCE\n :"))
    if option==1 :
         m=float(input("Enter amount :"))
         balance+=m
         print(m, "rupees deposited")
    elif option==2:
         p=float(input("Enter amount :"))
         if p>balance:
            print("Insufficient balance")
         else:
            balance-=p
            print(p,"rupees withdraw completed")
            print("amount remaining",balance)
    elif option==3:
           print("the amount present in your bank account : ",balance,'rupees')
    else:
         print("option not valid")
