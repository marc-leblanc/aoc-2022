f = open("input.txt", "r")

end_stacks = False
moves = []
stacks = []
new_move = ''
tststr = []
tstack = []
for line in f:
    if line[0] == 'm':
        new_move = line.replace("move ", '').rstrip('\n')
        new_move = new_move.replace(" from ", ',')
        new_move = new_move.replace(" to ",',')
        moves.append(new_move)
    elif len(line) > 0 and line[0] != 'm':
        tststr.append(line)
    else:
        end_stacks = True

stacks = len(tststr) -1 
cache = tststr[stacks-1].split()


for x in range ((stacks),-1, -1):
    mk = 0
    if x == (stacks):
        for y in range(len(cache)): 
            tstack.append([y+1])
    else:
        for marker in range(1, len(tststr[x]),4 ):
            if tststr[x][marker] != ' ' and tststr[x][marker].isnumeric() != 1:
                tstack[mk].append(tststr[x][marker])
            mk+=1

for makeMv in moves:
    tmove = makeMv.split(',')
    mvtop = len(tstack[int(tmove[1])-1]) 
    mvbot = mvtop - int(tmove[0]) 
    mvsrc = int(tmove[1]) -1 
    mvdst = int(tmove[2]) - 1
    mvstk = tstack[mvsrc][mvbot:mvtop+1]
    print (makeMv)
    print ('From:', tstack[mvsrc])
    print ('Move:', mvstk)
    print ('To  :',tstack[mvdst] )
    #for x in mvstk[::-1]: # Reverse order
    for x in mvstk: 
        tstack[mvdst].append(x)
    for x in range(mvtop, mvbot, -1):
        tstack[mvsrc].pop(x-1)
    print ('Src Stack:', tstack[mvsrc])
    print ('Dst Stack:', tstack[mvdst])



for lns in tstack:
    print(lns)

final = []
for stops in tstack:
    final.append(stops[len(stops)-1]) 
print ('Total Moves:', len(moves))
print ('First Move:', moves[0])
print ('Last Move:', moves[len(moves)-1])
print (str(final))
