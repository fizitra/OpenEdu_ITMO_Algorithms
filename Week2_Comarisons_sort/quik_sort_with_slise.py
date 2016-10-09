import random
from time import time

def QuickSort(A):
    if len(A) <= 1:
        return A
    else:
        q = random.choice(A)
        L = [elem for elem in A if elem < q]

        M = [q] * A.count(q)
        R = [elem for elem in A if elem > q]
        return QuickSort(L) + M + QuickSort(R)

A = [1000,0,1,0,1,0,1,0,1,0,0,0,1,1,1,0,2,9,9,9,2,2,2,0,0,0]
#A = [1,1,1,0,0,0]
start = time()
QuickSort(A)
print(A,time()-start)