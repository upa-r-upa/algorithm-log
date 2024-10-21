def solution(participant, completion):
    players = dict()
    
    for player in participant:
        players[player] = players.get(player, 0) + 1
        
    for player in completion:
        if players[player] > 1:
            players[player] -= 1
        else:
            del players[player]
            
    return list(players.keys())[0]