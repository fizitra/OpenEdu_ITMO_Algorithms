f = open("antiqs.in","r")
N = int(f.read())
f.close()
#A = [(lambda x:(x+N//2)%N+1 if x < N//2 +N%2 else N-x)(x)  for x in range(0,N)]
A = [x+1 for x in range(N)]
A = A[:N//2]+A[-1:-N//2-1:-1]
f = open("antiqs.out","w")
print(*A, file=f)
f.close()
