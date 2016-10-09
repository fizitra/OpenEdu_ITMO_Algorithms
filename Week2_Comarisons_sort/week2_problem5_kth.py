import array

def generate(n, A, B, C, a1, a2):
    arr = array.array('i',[0]*n)
    arr[0] = a1
    arr[1] = a2
    for i in range(2,n):
        if A * arr[i-2] + B * arr[i-1] + C >= 3:
            arr[i] = (A * arr[i-2] + B * arr[i-1] + C)%6 - 6
        else:
            arr[i] = A * arr[i-2] + B * arr[i-1] + C
    return arr


print(generate(5, 2, 3, 5, 1, 2))

