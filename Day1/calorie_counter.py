# Set an input file
f = open("input.txt", "r")
#Declare some vars and initialize them
sum = 0
heaviest = 0
sheaviest = 0
theaviest = 0
sumlist=[]
# we're gonna loop over the lines in the file
# and do some stuff
for line in f:
  x = line.rstrip('\n') # read in a line, and dump the \n break 
  if  x.isnumeric() > 0 : # if it is a number, add it to the sum
    sum = sum + int(x)
  else: 
    # if  it's not a number, check if we have a new winner for most calories
    if sum > heaviest:   
        heaviest = sum
    sumlist.append(sum) # add this elfs weight to a list
    sum = 0 # reset the sum

print("heaviest: ", heaviest) # print the biggest calorie count
sumlist.sort(reverse=True) # sort the calorie list so we can snag the top 3
print ("Top 3 Combined:", sumlist[0]+sumlist[1]+sumlist[2]) # print the weight of the top 3 combined