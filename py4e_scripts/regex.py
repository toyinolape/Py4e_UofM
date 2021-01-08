import re
#Extract the number from each of the lines using a regular expression and the findall() method. 
#Compute the average of the numbers and print out the average as an integer.
#Extracting Digits and Summing them
hand = open("e1206.txt") #opens the file 
numlist = [] #initiates the list 

for line in hand: #loop through the file 
    line = line.rstrip() # strips off whitespaces to the right
    extract = re.findall("([0-9]+)", line) #parses the line and puts it in a list 

    if len(extract) < 1 : continue #Fail safe incase there are no numbers, so it doesnt return an error

    for i in range(len(extract)): #loops through all the integers in the list 
        num = float(extract[i]) # maps the integers and makes them integers 
        numlist.append(num) # appends it to the new list

print(sum(numlist)/len(numlist)) #prints the average