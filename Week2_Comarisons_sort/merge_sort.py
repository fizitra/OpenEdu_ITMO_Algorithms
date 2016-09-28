'''
разбор алгоритма: http://foxford.ru/wiki/informatika/sortirovka-sliyaniem#!
'''

def merge(list_left,list_right):
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
    return  merge_list


def merge_sort(list_sort):
    if len(list_sort) < 2:
        return list_sort
    else:
        medium = len(list_sort)//2
        list_left = list_sort[:medium]
        list_right = list_sort[medium:]
        return merge(merge_sort(list_left),merge_sort(list_right))

if __name__ == '__main__':
    A = [1,0,2,2,0,1,2,2,3,4,1,0,5,4,3,2,1,0,1,2,3,4,5,5,4,4,2,9]
    print(merge_sort(A))
