from collections import deque
def eval_d(N):
    
    d=deque()
    for i in range(N):
        user=input().split()
        if len(user)>1:
            m,e=user[0],user[1]
        else:
            m=user[0]
        if m=='append':
            d.append(e)
        elif m=='appendleft':
            d.appendleft(e)
        elif m=='pop':
            d.pop()
        elif m=='popleft':
            d.popleft()
    return" ".join([i for i in d])
print(eval_d(int(input())))
        
