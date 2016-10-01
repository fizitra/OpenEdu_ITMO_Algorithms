'''
условие задачи:

Число инверсий

Имя входного файла: inversions.in
Имя выходного файла: inversions.out
Ограничение по времени: 2 секунды
Ограничение по памяти: 256 мегабайт

Инверсией в последовательности чисел A называется такая ситуация, когда i < j, а Ai > Aj.
Дан массив целых чисел. Ваша задача — подсчитать число инверсий в нем.
Подсказка: чтобы сделать это быстрее, можно воспользоваться модификацией сортировки слиянием.

Формат входного файла
В первой строке входного файла содержится число n (1<n<100 000) — число элементов в массиве. Во второй строке находятся n целых чисел, по модулю не превосходящих 109.

Формат выходного файла
В выходной файл надо вывести число инверсий в массиве.

Пример
inversions.in
inversions.out
10
1 8 2 1 4 7 3 2 3 6

17
'''


def merge(list_left, list_right, len_list_sort, len_left, len_right):
    '''
    merge - фукнкция слияния 2-х массивов
    :param list_left: левая половина сортируемого массива
    :param list_right: правая половина сортируемого массива
    :param len_list_sort: длина сортируемого массива
    :param len_left: длина левой половины сортируемого массива
    :param len_right: длина правой половина сортируемого массива
    :return: массив в котором все элементы отсортированы по возрастанию(неубыванию)
    '''
    global k
    merge_list = [None] * len_list_sort
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


def merge_sort(list_sort, len_list_sort):
    '''
    merge_sort - сортировка слиянием. На вход подаются два параметра
    :param list_sort: массив который необходимо отсортировать
    :param len_list_sort: длина этого массива в виде константы
    :return: возвращается отсортированный массив
    P.S. Алгоритм оптимизирован по производительности вместо len(list), работает O(N), вычисляется константа len_list за O(1)
         на тестах прирост производительности примерно в 15-25 раз
    '''
    if len_list_sort < 2:
        return list_sort
    else:
        medium = len_list_sort // 2
        len_left = len_list_sort // 2
        len_right = len_list_sort // 2 + len_list_sort % 2
        list_left = list_sort[:medium]
        list_right = list_sort[medium:]
        return merge(merge_sort(list_left, len_left), merge_sort(list_right, len_right), len_list_sort, len_left, len_right)

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
