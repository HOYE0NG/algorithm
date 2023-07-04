import sys
sys.setrecursionlimit(10**5)
from copy import deepcopy

def operator(n1, op, n2):
    if op == "+":
        return n1+n2
    if op == "-":
        return n1-n2
    if op == "*":
        return n1*n2

def dfs(start, target):
    global ans
    if start == N-1:
        ans = max(ans, target)
        return
    
    if start + 2 < N :
        dfs(start+2, operator(target, Equation[start+1], Equation[start+2]))
    if start + 4 < N :
        tmp = operator(Equation[start+2], Equation[start+3], Equation[start+4])
        dfs(start+4, operator(target, Equation[start+1], tmp))
        
N = int(input())
Equation = list(input())
ans = -pow(2, 31)
for i in range(0, len(Equation), 2):
    Equation[i] = int(Equation[i])
    
dfs(0, Equation[0])

print(ans)