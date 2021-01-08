#first read the file
fname = input("Enter file name: ")
fh = open (fname,"r")
count = 0
tot = 0
ans = 0
for lx in fh:
    #ly = lx.rstrip()
    if lx.startswith("X-DSPAM-Confidence: "):
        count = count+1
        value = lx.find("X-DSPAM-Confidence: ")
        number = lx[value+21:]
        num = float(number)
        tot = num + tot
print ("Average spam confdence:", tot/count)
