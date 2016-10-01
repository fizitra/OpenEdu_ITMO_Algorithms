def merge(list_left,list_right,N, len_left, len_right):
    global k
    merge_list = [None]*N
    i = 0
    j = 0
    n = 0
    while i < len_left and j < len_right:
        if list_left[i] <= list_right[j]:
            merge_list[n] = list_left[i]
            i += 1
            n += 1
        else:
            merge_list[n] = list_right[j]
            j += 1
            k += len_left - i
            n += 1
    if len_right - j:
        merge_list[n:] = list_right[j:]
    else:
        merge_list[n:] = list_left[i:]
    return  merge_list


def merge_sort(list_sort, N):
    if N < 2:
        return list_sort
    else:
        medium = N//2
        len_left = N//2
        len_right = N//2 + N%2
        list_left = list_sort[:medium]
        list_right = list_sort[medium:]
        return merge(merge_sort(list_left, len_left),merge_sort(list_right, len_right),N, len_left,len_right)

if __name__ == '__main__':
    from time import time
    f = open('inversions.in','r')
    A = [list(map(int,line.strip().split())) for line in f]
    f.close()
    k = 0
    #start = time()
    merge_sort(A[1], len(A[1]))
    #print(time()-start)
    f = open('inversions.out', 'w')
    f.write(str(k)+"\n")
    f.close()
    '''
    k = 0
    start = time()
    for i in range(len(A[1])):
        for j in range(i+1,len(A[1])):
            if i < j and A[1][i] > A[1][j]:
                k += 1
    print(time()-start)
    f = open('inversions.out', 'a')
    f.write(str(k))
    f.close()
    '''
