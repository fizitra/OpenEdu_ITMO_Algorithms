import random
from time import time


def quick_sort(massive, l, r):
    #
    global n
    if l >= r:
        # print('%s)'%n,'l=',l,'r=',r, massive)
        n += 1
        return
    else:
        q = random.choice(massive[l:r + 1])
        i = l
        j = r
        # print('%s)'%n,'q=',q,'l=',l,'r=',r,'\n', massive )
        n += 1
        while i <= j:
            while massive[i] < q:
                i += 1
                # print('i=',i,end=' ')
            while massive[j] > q:
                j -= 1
                # print('j=',j,end=' ')
            if i <= j:
                massive[i], massive[j] = massive[j], massive[i]

            # print('| massive['+str(i)+']', massive[i],'<->',massive[j],'massive['+str(j)+']', massive, 'l=%s r=%s i=%s->l j=%s->r'%(l, r, i+1, j-1))
                i += 1
                j -= 1
        quick_sort(massive, l, j)
        quick_sort(massive, i, r)


# A = [9,8,7,6,6,7,8,9,5,5,4,3,2,1,0,0,1,2,0,3]
# A = [1000,0,1,0,1,0,1,0,1,0,0,0,1,1,1,0,2,9,9,9,2,2,2,0,0,0]
A = [1, 2, 3, 3, 2, 1, 1, 3, 2, 1]
n = 1
start = time()
quick_sort(A, 0, len(A) - 1)
print(A, time()-start)
