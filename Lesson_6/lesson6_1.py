a=b'r\xc3\xa9sum\xc3\xa9'
b=a.decode()
print(b)
c=b.encode('Latin1')
print(c)
d=c.decode('Latin1')
print(d)