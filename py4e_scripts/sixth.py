
num = 0
largest = None
smallest = None
while True:
    snum = input("Enter a number: ")
    if snum == "done" :
        break
    try:
        num = int(snum)
    except:
        print("Invalid Input")
        continue
    if largest is None:
        largest = num
        smallest = num
    elif num > largest :
        largest = num
    elif num < smallest :
        smallest = num


print("Maximum", largest)
print("Minimun", smallest)
