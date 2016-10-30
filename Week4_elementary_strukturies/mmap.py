import mmap
with open("stack.in", "rt") as fin:
    mm = mmap.mmap(fin.fileno(), 0, access=mmap.ACCESS_READ)
    n = int(mm.readline().decode())
    for i in range(n):
        print(mm.readline().decode().strip())