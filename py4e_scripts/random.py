a = [0,2,4,6]
result =""

for i in range(len(a)): #iterates the length of list "a" number of times  
    
    result += str(i + a[i])# takes the value of the "i" position in "a" list and adds it to "i" 
#it then puts that value in reult as astring and concatenates until the for loop is exhausted 
print(result)