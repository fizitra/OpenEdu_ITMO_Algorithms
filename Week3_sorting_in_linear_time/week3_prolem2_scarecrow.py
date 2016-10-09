with open('scarecrow.in', 'r') as fin:
    n, k = map(int,fin.readline().split())
    matr_list = list(map(int,fin.readline().split()))
    buc_list =[[] for x in range(k)]
    '''
        список matr_list разбиваем на карманы размера k по принципу: в 0 карман попадают элементы
        0, k, 2*k , ... , n//k*k  в 1-й карман - эл-ты 1, k+1, ... , n//k*k + 1 и.т.д. для того чтобы
        карманы были равной длины заполняем карман значением -1, если елементы в списке matr_list
        закончились. По по мере добавления элементов в каждый карман проводим его сортировку вставками.
        на выходе получаем buk_list - список отсортированных карманов.
    '''
    for i in range(k):
        count = 0
        for j in range(i,(n+k-1)//k*k,k):
            if j < n:
                buc_list[i].append(matr_list[j])
            else:
                buc_list[i].append(-1)
            new_count = count
            while new_count > 0 and buc_list[i][new_count] != -1 and new_count > 0 and buc_list[i][new_count] < buc_list[i][new_count-1]:
                buc_list[i][new_count], buc_list[i][new_count-1] = buc_list[i][new_count-1], buc_list[i][new_count]
                new_count -= 1
            count += 1
with open('scarecrow.out','w') as fout:
    '''
        элементы списка buc_list переносим обратно в matr_list по следующему принципу, сначала все
        0-е элементы c 0 строки по к-1-ю, потом 1-е элементы и т.д до (n+k-1)//k, элементы значение
        которых равно -1 в список не заносятся. Пока переносим, сравниваем поступивший
        элемент с предыдущим, если поступивший элемент меньше, значит исходный список matr_list
        не возможно отсортировать сортировкой пугалом. Если всегда поступивший элемент больше предыдущего,
        то заполнение matr_list проходит до конца и значение count становится больше n, сортировка пугалом
        завершена успешно
    '''
    count = 0
    flag = False
    for j in range((n+k-1)//k):
        for i in range(k):
            if buc_list[i][j] != -1:
                matr_list[count] = buc_list[i][j]
                if count > 0 and matr_list[count] < matr_list[count - 1]:
                    print('NO', file=fout)
                    flag = True
                    break
                count += 1
        if flag:
            break
    if count > n-1:
        print('YES', file=fout)