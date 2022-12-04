f = open("input.txt", "r")
count = 0
overlap_count = 0
for line in f:
    ids = line.rstrip('\n').split(',')
    r1_min = int(ids[0].split('-')[0])
    r1_max = int(ids[0].split('-')[1])
    r1 = range(r1_min,r1_max+1)
    
    r2_min = int(ids[1].split('-')[0])
    r2_max = int(ids[1].split('-')[1])
    r2 = range(r2_min,r2_max+1)

    if r1_min <= r2_min and r1_max >= r2_max:
        count += 1
    elif r2_min <= r1_min and r2_max >= r1_max:
        count += 1
    overlap = set(r1).intersection(r2)
    if len(overlap) > 0:
        overlap_count += 1

print (count)
print (overlap_count)