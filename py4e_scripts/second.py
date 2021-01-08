hrs = input("Enter Hours:")
h = float(hrs)
Rate = input("Enter rate: ")
r = float(Rate)

if h > 40:
    h = (h-40) * (1.5)+40
else:
    h = h *1

GrossPay = (h*r)
GP= (GrossPay)
print  (GP)
