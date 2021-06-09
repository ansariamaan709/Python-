a=[100,50,40]
num_score=int(input('Enter the number of score'))
for k in range(num_score):
    player_score=int(input('Enter the player score '))
    a.append(player_score)
    a.sort(reverse=True)
    print(a.index(player_score))
print(a)