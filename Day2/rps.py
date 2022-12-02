# A X = Rock (1)
# B Y = Paper (2)
# C Z = Scissors (3)

score = 0
rscore = 0 # "Real" score
f = open("input.txt", "r")
for line in f:
    throw = line.split()
    # IF ROCK
    if throw[1] == "X" and throw[0] == "A":  # ROCK vs ROCK
        score = score + 1 + 3
        rscore = rscore + 3 + 0
    elif throw[1] == "X" and throw[0] == "B": # ROCK vs PAPER
        score = score + 1 + 0
        rscore = rscore + 1 + 0
    elif throw[1] == "X" and throw[0] == "C": # ROCK vs SCISSORS
        score = score + 1 + 6
        rscore = rscore + 2 + 0
    # IF Paper
    elif throw[1] == "Y" and throw[0] == "A":  # PAPER vs ROCK
        score = score + 2 + 6
        rscore = rscore + 1 + 3
    elif throw[1] == "Y" and throw[0] == "B": # PAPER vs PAPER
        score = score + 2 + 3
        rscore = rscore + 2 + 3
    elif throw[1] == "Y" and throw[0] == "C": # PAPER vs SCISSORS
        score = score + 2 + 0
        rscore = rscore + 3 + 3
    # IF Paper
    elif throw[1] == "Z" and throw[0] == "A": # SCISSORS vs ROCK
        score = score + 3 + 0
        rscore = rscore + 2 + 6
    elif throw[1] == "Z" and throw[0] == "B": # SCISSORS vs PAPER
        score = score + 3 + 6
        rscore = rscore + 3 + 6
    elif throw[1] == "Z" and throw[0] == "C": # SCISSORS vs SCISSORS
        score = score + 3 + 3
        rscore = rscore + 1 + 6 
    throw.clear()    
print ("Total Score: ", score)
print ("Real Score :", rscore)