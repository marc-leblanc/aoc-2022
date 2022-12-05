f = open("input.txt", "r")
import re
end_stacks = False
moves = []
stacks = []
new_move = ''
for line in f:
    if line[0] == 'm':
        print ("Moves")
        new_move = line.replace("move ", '').rstrip('\n')
        new_move = new_move.replace(" from ", ',')
        new_move = new_move.replace(" to ",',')
        moves.append(new_move)
    elif line[1] == '1':
        end_stacks = True
    else:
        stacks.append(line.replace(' ','').rstrip('\n'))

print (stacks)
#my_str = 'a1s2d3f4g5'

#result = re.sub(r'[^0-9]', '', my_str)

#print(result)  # 👉️ '12345'