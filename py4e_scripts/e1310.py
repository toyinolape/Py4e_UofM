import urllib.request, urllib.parse, urllib.error
import ssl
import json


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

acct = input('Enter Link:') #stores the URL Link 
print('Retrieving', acct) #Just shows the link 

connection = urllib.request.urlopen(acct, context=ctx) #ths is supposed to open the link 
data = connection.read().decode()# decode the bits and converts to readable string / UTF-8
print ("Retrieved", len(data), "characters")

js = json.loads(data) # parses the JSON
#print(json.dumps(js, indent=4)) # organized print/ 4 space indentation

inc = 0
num = 0

for u in js['comments']: 
    
    inc += 1
    num += u['count']
    
print ("Count:", inc)
print ("Sum:", num)

        
        