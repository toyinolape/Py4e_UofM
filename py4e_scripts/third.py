Hrs = input("Enter hours: ")
h = float(Hrs)
Rate = input("Enter rate: ")
r = float(Rate)
if h > 40:
    GrossPay = ((h-40) * (1.5*10.50))+(40 *10.50)
    print("we move")
else :
    print("we move")
GP = str(GrossPay)
print ("Your gross pay is ", GP)
