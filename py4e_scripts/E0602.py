text = "X-DSPAM-Confidence:    0.8475";
value = text.find(":")
start = int(value)
#print(value)
number = text[start+1:40]
print(number.strip())
