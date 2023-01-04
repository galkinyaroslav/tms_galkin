a = input('введите первую строку')
b = input('введите вторую строку')
c = input('введите третью строку')
d = input('введите четвертую строку')

with open('file.txt', 'w') as file:
    file.write(a + '\n')
    file.write(b + '\n')
    # file.close()
with open('file.txt', 'a+') as file:
    file.write(c + '\n')
    file.write(d + '\n')
with open('file.txt', 'r') as file:
    print(file.read())
