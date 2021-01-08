fn = input("Enter file name:")
if len(fn) < 1:
    fn = "mbox-short.txt"
fh = open(fn)
hour = dict()
hours =list()
count = 0
for line in fh:
    if line.startswith("From "):
        #print(line)
        words = line.split()
        times = words[5]
        toyin = times.split(":")
        hours.append(toyin[0])
#print (hours)

for time in hours:
           hour[time] = hour.get(time, 0) + 1

for x, y in sorted(hour.items()):
    print (x,y)
