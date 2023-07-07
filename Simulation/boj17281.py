from itertools import permutations

N = int(input())
team = [list(map(int, input().split())) for _ in range(N)]
cases = list(permutations([1,2,3,4,5,6,7,8], 8))

score = 0
result = 0

for case in cases:
    order = list(case[0:3]) + [0] + list(case[3:8])
    start = 0
    score = 0
    for inning in range(N): # inning
        out = 0
        ru1 = 0
        ru2 = 0
        ru3 = 0
        home = 0
        while out < 3:
            for i in range(start, 9):
                hit = team[inning][order[i]]
                if hit == 0:
                    out += 1
                elif hit == 1:
                    if ru3 == 1:
                        ru3 = 0
                        home += 1
                    if ru2 == 1:
                        ru2 = 0
                        ru3 = 1
                    if ru1 == 1:
                        ru1 = 0
                        ru2 = 1
                    ru1 = 1
                elif hit == 2:
                    if ru3 == 1:
                        ru3 = 0
                        home += 1
                    if ru2 == 1:
                        ru2 = 0
                        home += 1
                    if ru1 == 1:
                        ru1 = 0
                        ru3 = 1
                    ru2 = 1
                elif hit == 3:
                    if ru3 == 1:
                        ru3 = 0
                        home += 1
                    if ru2 == 1:
                        ru2 = 0
                        home += 1
                    if ru1 == 1:
                        ru1 = 0
                        home += 1
                    ru3 = 1    
                elif hit == 4:
                    if ru3 == 1:
                        ru3 = 0
                        home += 1
                    if ru2 == 1:
                        ru2 = 0
                        home += 1
                    if ru1 == 1:
                        ru1 = 0
                        home += 1
                    home += 1   
                if out == 3:
                    start = (i+1)%9
                    break 
                else :
                    score += home
                    home = 0
            if out != 3:
                start = 0
    
    if score > result:
        result = score
                
                         
print(result)