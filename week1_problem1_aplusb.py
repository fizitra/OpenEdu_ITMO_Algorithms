file = open('aplusb.in','r')
a,b = map(int,file.read().split())
file.close()
file = open('aplusb.out','w')
file.write(str(a+b)+'\n')
file.close()
#Задание сдано