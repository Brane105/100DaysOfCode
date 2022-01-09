#TIP CALCULATOR 
#enter the Bill 
#enter the number of members 
print("$.Welcome To TIP Calculator.$")
bill = float(input("enter the Bill $ : "))
m = int(input("Enter the number of Memebers : "))
#choose the tip you ll give out 
select = (int(input("Select the Tip : 10 , 12 , 15 : \n =")))
#statments
if select == 10:
  #bill with tip 
    print("bill_with_tip : {0:.2f}$".format(bill*1.10))
    print("Each person should pay {0:.2f}$".format(bill*1.10/m))
elif select == 12:
    print("bill_with_tip : {0:.2f}$".format(bill*1.12))
    print("Each person should pay {0:.2f}$".format(bill*1.12/m))
elif select == 15:
    print("bill_with_tip : {0:.2f}$".format(bill*1.15))
    print("Each person should pay {0:.2f} $".format((bill*1.15/m)))
else :
    print("Invalid Input")
  #print the invlid  
         
     

