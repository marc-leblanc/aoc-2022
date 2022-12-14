from collections import Counter

f = open("input.txt", "r")
found = False
cbuffer = []
for line in f:
    charcount=0
    marker =0 
    for char in line:
        while found == False:
            charcount +=1
            if charcount >13:
                keycount = len(Counter(line[charcount-14:charcount]).keys())
                if keycount == 14:
                    marker = charcount
                    found = True

print (marker)