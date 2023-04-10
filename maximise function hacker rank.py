from itertools import *

K, M = map(int, raw_input().split())
N = []

for _ in xrange(K):
     N.append(map(int, raw_input().split())[1:])        
MAX = -1
for i in product(*N):
    MAX = max(sum(map(lambda x: x**2, i))%M, MAX)
    
print MAX
