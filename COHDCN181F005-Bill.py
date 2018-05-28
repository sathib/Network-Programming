import sys
import os

def bilcal():
    filename="Final_Bill.txt"
    accessmode="a"
    file=open(filename,accessmode)
    
    item=0
    qun=0
    totalpri=0
    print("\n***************************************************************")
    billno=int(input("\n\t\t\t\t\tBil Number= "))
    CaNa=str(input("\n\t\t\t\t\tCashier Name= "))
    CaID=int(input("\n\t\t\t\t\tCashier ID= "))
    
    while True:
        try:
            pri=float(input("\nPrice of the Good= Rs "))
            qun=float(input("Quntity of Goods= "))
            item=pri*qun
            totalpri=totalpri+item
   
        except ValueError as e:
            break
        
    if totalpri>=5000:
        s=totalpri*0.12
        totalpay=totalpri-s
            
    elif totalpri>=3000:
        s=totalpri*0.10
        totalpay=tot-s
       
    elif totalpri>=1000:
        s=totalpri*0.05
        totalpay=totalpri-s
      
    else:
        s=0
        totalpay=totalpri
       
    
    print("\n\t\t\tPrice:Rs %.2f" % totalpri)
    print("\t\t\tDiscount:Rs %.2f" % s)
    print("\t\t\tTotal Payable Value :Rs %.2f" % totalpay)
    print("\n***************************************************************")
   
    file.write("\n\n\n\n*******************************************************************")
    file.write("\n\n\t\t\t\t\t---Bil Number: %.2d" % billno)
    file.write("\n\t\t\t\t\t---Cashier Name: %.2s" % CaNa)
    file.write("\n\t\t\t\t\t---Cashier ID: %.2d" % CaID)
    file.write("\n\n\n\t*)Your Price Is :Rs %.2f" % totalpri)
    file.write("\n\t*)Discount Value is :Rs %.2f" % s)
    file.write("\n\t*)Payable Value :Rs %.2f" % totalpay)
    file.write("\n\n\nThank You.! Come Again.!")
    file.write("\n\n*******************************************************************")
    file.close()
    
bilcal()
