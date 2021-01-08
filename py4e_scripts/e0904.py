name = input("Enter file name:")
#if len(name) < 1 : name = "mbox-short.txt"
words = dict()
fa = open(name)
count = 0
for line in fa:

    if line.startswith("From"):
    count = count +1
    print(line[1], count)
