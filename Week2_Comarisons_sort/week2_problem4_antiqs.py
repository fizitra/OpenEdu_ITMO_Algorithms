def uqs(A):
    if len(A) < 3:
        return A
    elif len(A)%2:
        M = [A[-1]]
        L = A[:len(A)//2-1] + M
        R = A[len(A)//2-1:-1]
        #print('2',L,M,R)
        return uqs(L) + uqs(R)
    else:
        M = [A[-1]]
        L = A[:len(A)//2-1] + M
        R = A[len(A)//2-1:-1]
        #print('1',L,M,R)
        return uqs(L) + uqs(R)

f = open("antiqs.in","r")
N = int(f.read())
f.close()
A = [N-x for x in range(N)]
f = open("antiqs.out","w")
print(*uqs(A), file=f)
f.close()
