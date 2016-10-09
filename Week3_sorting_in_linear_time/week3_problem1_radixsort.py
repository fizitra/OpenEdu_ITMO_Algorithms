with open('radixsort.in', 'r') as radix:
    n,m,k = map(int,radix.readline().split())
    matrix = [[None]*m for x in range(n)]
    for j in range(m):
        line = list(radix.readline().strip())
        for i in range(m):
            matrix[i][j] = line[i]
            #matrix[]
            #i += 1
    matrix = list(zip(range(m),matrix))
    print(matrix)