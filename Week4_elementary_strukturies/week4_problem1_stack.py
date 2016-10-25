import mmap
with open('stack.in','rt') as fin:
    mm = mmap.mmap(fin.fileno(), 0, access=mmap.ACCESS_READ)
    n = int(mm.readline().decode())
    stack_in = [None]*n
    stack_out = []
    i = 0
    for j in range(n):
        line = mm.readline().decode().strip().split()
        if line[0] == "+":
            stack_in[i] = line[1]
            i += 1
        else:
            i -= 1
            stack_out.append(stack_in[i])
            stack_in[i] = None

with open('stack.out', 'w') as fout:
    print(*stack_out, sep='\n', file=fout)