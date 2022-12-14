tststr = "        [G]         [D]     [Q]    " + ' '
tstack = []
stack_count = 0
print ("length:", len(tststr))

for x in range(0, len(tststr),4):
    print (tststr[x+1])  
    if len(tstack) < 1 and tststr != ' ':
        tstack.append(tststr[x+1])
    elif tststr[x+1] != ' ':
       tstack[stack_count].append(tststr[x+1])
    stack_count += 1
print (tstack)