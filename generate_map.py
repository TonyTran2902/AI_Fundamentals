import numpy as np
'''
Input only includes Wumpus(W), Pit(P), Agent(A) and Gold(G), Poisonous Gas(P_G), 
Healing Potions(H_P). 
You need to update information about Stench(S)-W, Breeze(B)-P, 
Whiff(W_H)-P_G and Glow(G_L)-H_P on the map based on input data.
'''

'''
Breeze: Indicates an adjacent cell contains a pit.
Stench: Indicates an adjacent cell contains the Wumpus.
Scream: Heard if the Wumpus is killed.
Whiff: Indicates an adjacent cell contains poisonous gas.
Glow: Indicates an adjacent cell contains a healing potion.
'''

def check_index(map_size, index):
    if index < 0 or index > map_size - 1:
        return False
    return True

def breeze_preprocess(raw_map, map_size, i, j):
    if check_index(map_size, j + 1) == True:
        if(raw_map[i][j + 1] == '-'):
            raw_map[i][j + 1] = ''
            raw_map[i][j + 1] +='B'
        elif('B' in raw_map[i][j + 1]):
            None
        else:
            raw_map[i][j + 1] +='B'
    
    if check_index(map_size, i + 1) == True:
        if(raw_map[i + 1][j] == '-'):
            raw_map[i + 1][j] = ''
            raw_map[i + 1][j] +='B'
        elif('B' in raw_map[i + 1][j]):
            None
        else:
            raw_map[i + 1][j] +='B'
            
    if check_index(map_size, i - 1) == True:
        if(raw_map[i - 1][j] == '-'):
            raw_map[i - 1][j] = ''
            raw_map[i - 1][j] +='B'
        elif('B' in raw_map[i - 1][j]):
            None
        else:
            raw_map[i - 1][j] +='B'
            
    if check_index(map_size, j - 1) == True:
        if(raw_map[i][j - 1] == '-'):
            raw_map[i][j - 1] = ''
            raw_map[i][j - 1] +='B'
        elif('B' in raw_map[i][j - 1]):
            None
        else:
            raw_map[i][j - 1] +='B'

def stench_preprocess(raw_map, map_size, i, j):
    if check_index(map_size, j + 1) == True:
        if(raw_map[i][j + 1] == '-'):
            raw_map[i][j + 1] = ''
            raw_map[i][j + 1] += 'S'
        elif('S' in raw_map[i][j + 1]):
            None
        else:
            raw_map[i][j + 1] += 'S'
    
    if check_index(map_size, i + 1) == True:
        if(raw_map[i + 1][j] == '-'):
            raw_map[i + 1][j] = ''
            raw_map[i + 1][j] += 'S'
        elif('S' in raw_map[i + 1][j]):
            None
        else:
            raw_map[i + 1][j] += 'S'
            
    if check_index(map_size, i - 1) == True:
        if(raw_map[i - 1][j] == '-'):
            raw_map[i - 1][j] = ''
            raw_map[i - 1][j] +='S'
        elif('S' in raw_map[i - 1][j]):
            None
        else:
            raw_map[i - 1][j] +='S'
            
    if check_index(map_size, j - 1) == True:
        if(raw_map[i][j - 1] == '-'):
            raw_map[i][j - 1] = ''
            raw_map[i][j - 1] +='S'
        elif('S' in raw_map[i][j - 1]):
            None
        else:
            raw_map[i][j - 1] +='S'

def whiff_preprocess(raw_map, map_size, i, j):
    if check_index(map_size, j + 1) == True:
        if(raw_map[i][j + 1] == '-'):
            raw_map[i][j + 1] = ''
            raw_map[i][j + 1] += 'W_H'
        elif('W_H' in raw_map[i][j + 1]):
            None
        else:
            raw_map[i][j + 1] += 'W_H'
    
    if check_index(map_size, i + 1) == True:
        if(raw_map[i + 1][j] == '-'):
            raw_map[i + 1][j] = ''
            raw_map[i + 1][j] += 'W_H'
        elif('W_H' in raw_map[i + 1][j]):
            None
        else:
            raw_map[i + 1][j] += 'W_H'
            
    if check_index(map_size, i - 1) == True:
        if(raw_map[i - 1][j] == '-'):
            raw_map[i - 1][j] = ''
            raw_map[i - 1][j] +='W_H'
        elif('W_H' in raw_map[i - 1][j]):
            None
        else:
            raw_map[i - 1][j] +='W_H'
            
    if check_index(map_size, j - 1) == True:
        if(raw_map[i][j - 1] == '-'):
            raw_map[i][j - 1] = ''
            raw_map[i][j - 1] +='W_H'
        elif('W_H' in raw_map[i][j - 1]):
            None
        else:
            raw_map[i][j - 1] +='W_H'

def glow_preprocess(raw_map, map_size, i, j):
    if check_index(map_size, j + 1) == True:
        if(raw_map[i][j + 1] == '-'):
            raw_map[i][j + 1] = ''
            raw_map[i][j + 1] += 'H_P' 
        elif('H_P' in raw_map[i][j + 1]):
            None
        else:
            raw_map[i][j + 1] += 'H_P'
    
    if check_index(map_size, i + 1) == True:
        if(raw_map[i + 1][j] == '-'):
            raw_map[i + 1][j] = ''
            raw_map[i + 1][j] += 'H_P'
        elif('H_P' in raw_map[i + 1][j]):
            None
        else:
            raw_map[i + 1][j] += 'H_P'
            
    if check_index(map_size, i - 1) == True:
        if(raw_map[i - 1][j] == '-'):
            raw_map[i - 1][j] = ''
            raw_map[i - 1][j] +='H_P'
        elif('H_P' in raw_map[i - 1][j]):
            None
        else:
            raw_map[i - 1][j] +='H_P'
            
    if check_index(map_size, j - 1) == True:
        if(raw_map[i][j - 1] == '-'):
            raw_map[i][j - 1] = ''
            raw_map[i][j - 1] +='H_P'
        elif('H_P' in raw_map[i][j - 1]):
            None
        else:
            raw_map[i][j - 1] +='H_P'


def generate_map(map_filename):
        file = open(map_filename, 'r')

        map_size = int(file.readline())
        raw_map = [line.split('.') for line in file.read().splitlines()]
        for i in range (map_size):
            for j in range (map_size):
                if raw_map[i][j] == 'W':
                    stench_preprocess(raw_map, map_size, i, j)
                elif raw_map[i][j] == 'P':
                    breeze_preprocess(raw_map, map_size, i, j)
                elif raw_map[i][j] == 'P_G':
                    whiff_preprocess(raw_map, map_size, i, j)
                elif raw_map[i][j] == 'G_L':
                    glow_preprocess(raw_map, map_size, i, j)
        print(np.array(raw_map))
generate_map("map_1.txt")