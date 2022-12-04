f = open("input.txt", "r")
compartment = []
sum=0
dups = []
elf = 0
group = []
gsum = 0
groupbadge = ''
gbadge = {}
for line in f:
    compartment[:0] = line
    group.append(line)

    if elf == 2:
        gbadge = set.intersection(*map(set,group))
        elf = 0
        print ('Group Badge:', list(gbadge)[0])
        groupbadge = list(gbadge)[0]
        if ord(groupbadge)-96 >= 1 and ord(groupbadge)-96 <= 26:
            gsum = gsum + ord(groupbadge) - 96
        elif ord(groupbadge)-38 >= 27 and ord(groupbadge)-38 <= 53:
            gsum = gsum + ord(groupbadge) - 38
        group.clear()
    else:
        elf=elf+1
    c1 = line[:len(line)//2]
    c2 = line[len(line)//2:]
    dups[:0] = ''.join(set(c1).intersection(c2))
    for item in dups: 
        if ord(item)-96 >= 1 and ord(item)-96 <= 26:
            sum = sum + ord(item) - 96
        elif ord(item)-38 >= 27 and ord(item)-38 <= 53:
            sum = sum + ord(item) - 38
    dups.clear()
print ('Sum: ', sum)
print ('Group Sum:', gsum)