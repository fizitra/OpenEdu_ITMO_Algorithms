file = open('sortland.in', 'r')
input_list = [line.strip() for line in file]
file.close()
#prinst(input_list)
sortland_list = {list(map(float,input_list[1].split()))[i-1]:i for i in range(1,int(input_list[0])+1)}
sortland_sort = sorted(list(map(float,input_list[1].split())))

file = open('sortland.out','w')
file.write(' '.join([str(x) for x in [sortland_list[sortland_sort[0]],sortland_list[sortland_sort[int(input_list[0])//2]],sortland_list[sortland_sort[-1]]]])+'\n')
file.close()