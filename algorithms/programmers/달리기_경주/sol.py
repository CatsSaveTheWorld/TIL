#%%
def solution(players, callings):
    result = {player: i for i, player in enumerate(players)} # 선수: 등수
    for who in callings:
        idx = result[who] # 호명된 선수의 현재 등수
        result[who] -= 1 # 하나 앞 등수로 바꿔줌 -1
        result[players[idx-1]] += 1 # 앞에 위치했던 선수의 등수 +1
        players[idx-1], players[idx] = players[idx], players[idx-1] # 위치 변경
    return players

#%%
def solution(players, callings):
    last_seq = 1

    while last_seq:
        same_call = []
        
        for i, call in enumerate(callings):
            print(f'-------{i}-------')
            print(f'callings : {callings}')
            print(f'call : {call}')
            if len(callings) == 0:
                break
            if len(same_call) == 0:
                same_call.append(callings[i])
                print(f'same_call : {same_call}')
                print(f'-------{i}-------')
            else:
                if call == same_call[0]:
                    same_call.append(callings[i])
                    print(f'same_call : {same_call}')
                    print(f'-------{i}-------')
                else:
                    break
        location = players.index(same_call[0])
        move_cnt = len(same_call)
        callings = callings[move_cnt:]
        print('same_call 생성 종료')
        print(f'callings : {callings}')
        print(f'location : {location}')
        print(f'move_cnt : {move_cnt}')

        if len(same_call) >= 2:
            del players[location]
            players.insert(location - move_cnt, same_call[0])
        else:
            players[location], players[location-1] = players[location-1], players[location]
        print(f'players : {players}')
        print()
        
        if len(callings) <= 1:
            last_seq = 0
    return players

players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]
