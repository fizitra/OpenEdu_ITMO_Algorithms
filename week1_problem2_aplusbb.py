file = open('aplusbb.in','r')
a,b = map(int,file.read().split())
file.close()
file = open('aplusbb.out','w')
file.write(str(a+b**2)+'\n')
file.close()
#Задание сдано
#Не отображается в GitHub