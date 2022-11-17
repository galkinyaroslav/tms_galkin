# 1
a=float(input('Input a: '))
b=float(input('Input b: '))
print('SUMM: ', a+b)
print('SUBSTACT: ', a-b)
print('POW: ', pow(a,b))
print('MOD: ', a%b)
print('DIV: ', a//b)

# 2
x=17/2*3+2
print(x)
x1=((17/2)*3)+2
print("parentheses ",x1)

x=2+17/2*3
print(x)
x1=2+((17/2)*3)
print("parentheses ",x1)

x=19%4+15/2*3
print(x)
x1=(19%4)+((15/2)*3)
print("parentheses ",x1)

x=(15+6)-10*4
print(x)
x1=(15+6)-(10*4)
print("parentheses ",x1)

x=17/2%2*3**3
print(x)
x1=((17/2)%2)*(3**3)
print("parentheses ",x1)

# 3
x=a
y=b
print((abs(x)-abs(y))/(1+abs(x*y)))

# addition
# 1
initstr='aaaaaBccBddBeeBffBggB'
newstr=initstr[5::3]
print('initstr ',initstr)
print('newstr ',newstr)
# 2
initstr2='AAAABBBBCCCCDDDDFFFF'
copyinitstr2=initstr2[0:4]+initstr2[4:8]+initstr2[8:12]+initstr2[12:16]+initstr2[16:]
print('initstr2 ',initstr2)
print('copyinitstr2 ',copyinitstr2)
# 3
initstr3='PYTHON'
newstr3=initstr3[::-1]
print(newstr3)
