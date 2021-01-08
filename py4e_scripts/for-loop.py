file = input("Enter file name: ")
numlines = 0
numwords = 0
numchar = 0
fh = open(file,"r")
for line in fh:
     numlines += 1
     numwords += len(line.split())
     numchars =+ len(line)
print ( numlines,numwords, numchars)
