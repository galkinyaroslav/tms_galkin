value= int(input('Введите целое число: '))
fsumm=0
for i in range(1,value+1):
    fsumm+=pow(i,3)
print(fsumm)
wsumm=0
while value>0:
    wsumm+=pow(value,3)
    value-=1
print(wsumm)