'''
Дан массив целых чисел. Ваша задача — отсортировать его в порядке
неубывания с помощью сортировки слиянием.
Чтобы убедиться, что Вы действительно используете сортировку слиянием,
мы просим Вас, после каждого осуществленного слияния, выводить индексы
граничных элементов и их значения.
'''

def merge(list_left,list_right, li, f):
    merge_list = []
    i = 0
    j = 0
    while i < len(list_left) and j < len(list_right):
        if list_left[i] < list_right[j]:
            merge_list.append(list_left[i])
            i += 1
        else:
            merge_list.append(list_right[j])
            j += 1
    merge_list += list_left[i:] + list_right[j:]
    print(1+li, len(merge_list)+li, merge_list[0], merge_list[-1], file=f)
    return  merge_list


def merge_sort(list_sort, li, f, l=0):
    # li индекс начала подстроки в исходной строке, l длина левой части подстроки в предыдущем разбиении
    li += l
    if len(list_sort) < 2:
        print(1+li, len(list_sort)+li, list_sort[0], list_sort[-1], file=f)
        return list_sort
    else:
        medium = len(list_sort)//2
        list_left = list_sort[:medium]
        list_right = list_sort[medium:]
        return merge(merge_sort(list_left, li, f, l=0), merge_sort(list_right, li, f, l=len(list_left)),li,f)

f = open('sort.in','r')
A = [line.strip() for line in f]
f.close()

list_sort = list(map(int,A[1].split()))
li = 0

f = open('sort.out','a')
print(*merge_sort(list_sort,li,f), file = f)