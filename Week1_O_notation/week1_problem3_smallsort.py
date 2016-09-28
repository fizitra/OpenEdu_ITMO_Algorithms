file = open('smallsort.in','r')
input_data_list = [line.strip() for line in file]
file.close()

#N = int(input_data_list[0])
sort_list = list(map(int,input_data_list[1].split()))

#для сортировки списка sort_list используем сортировку вставками
'''
for i in range(1,len(sort_list)):
    j = i-1
    while j >= 0 and sort_list[j] > sort_list[j+1]:
        sort_list[j+1], sort_list[j] = sort_list[j], sort_list[j+1]
        j -= 1
'''
sort_list.sort()
#print(sort_list)
file = open('smallsort.out','w')
file.write(' '.join([str(x) for x in sort_list])+'\n')
file.close()
#Задача сдана
#При использовании алгоритма сортировки вставками сбой на 6 тесте превышение времени работы программы