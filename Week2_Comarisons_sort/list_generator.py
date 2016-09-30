from random import randint, random

def list_generator(N, k, precision):
    new_list = [str(randint(0, k)) for i in range(N)]
    return new_list

if __name__ == '__main__':
    N = int(input())
    k = int(input())
    precision = int(input())
    name_of_file = input()
    file = open(name_of_file+'.in','w')
    file.write(str(N)+'\n'+' '.join(list_generator(N, k, precision))+'\n')
    file.close()
