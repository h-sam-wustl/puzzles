import numpy as np
results = np.genfromtxt('results.csv', delimiter=' ', dtype='str')

value_mapping = {'Z': 'C', 'Y': 'B', 'X': 'A'}
mapping=np.vectorize(lambda x: value_mapping.get(x, x))

results[:,1]=mapping(results[:,1])

total_score=0
for result in results:
    game_score=0
    if result[0]==result[1]:
        game_score+=3
    if result[1]=='A':
        game_score+=1
        if result[0]=='C':
            game_score+=6
    if result[1]=='B':
        game_score+=2
        if result[0]=='A':
            game_score+=6
    if result[1]=='C':
        game_score+=3
        if result[0]=='B':
            game_score+=6
    total_score+=game_score
    

def play(opp_play,result):
    your_play=''
    win_dict={'C': 'A', 'B': 'C', 'A': 'B'}
    lose_dict={'A': 'C', 'B': 'A', 'C': 'B'}
    if result=='Y':
        your_play=opp_play
    if result=='Z':
        your_play=win_dict[opp_play]
    if result=='X':
        your_play=lose_dict[opp_play]
    return your_play

total_score=0
for result in results:
    your_play=play(result[0],result[1])
    game_score=0
    if result[0]==your_play:
        game_score+=3
    if your_play=='A':
        game_score+=1
        if result[0]=='C':
            game_score+=6
    if your_play=='B':
        game_score+=2
        if result[0]=='A':
            game_score+=6
    if your_play=='C':
        game_score+=3
        if result[0]=='B':
            game_score+=6
    total_score+=game_score