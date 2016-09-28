'''
В первом варианте программы предполагалось создание словаря с индексами
всех элементов, операция в данной задаче не нужная, т.к. список по сути
есть словарь с ключами равными омеру индекса, кроме того, как оказалось
при тестировании, операция исключительно затратная по времени print('2')
'''
#все
#from time import time
#start = time()

file = open('sortland.in', 'r')
input_list = [line.strip() for line in file]
file.close()

#print('1',time()-start)
#start = time()

#prinst(input_list)
#sortland_list = {list(map(float,input_list[1].split()))[i-1]:i for i in range(1,int(input_list[0])+1)}
#print('2',time()-start)
#start = time()

sortland_list = list(map(float,input_list[1].split()))
sortland_sort = sorted(sortland_list)

#print('3',time()-start)
#start = time()

file = open('sortland.out','w')
#file.write(' '.join([str(x) for x in [sortland_list[sortland_sort[0]],sortland_list[sortland_sort[int(input_list[0])//2]],sortland_list[sortland_sort[-1]]]])+'\n')
file.write("{:} {:} {:}\n".format(sortland_list.index(sortland_sort[0])+1,sortland_list.index(sortland_sort[int(input_list[0])//2])+1,sortland_list.index(sortland_sort[-1])+1))
file.close()

#print('4',time()-start)
