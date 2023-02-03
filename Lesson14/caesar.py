txt='asd'
sh=40
# en_dictionary, en_dictionary_upper = "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# ru_dictionary, ru_dictionary_upper = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя", "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def caesar(values,shift):
    b=values.encode(encoding='ascii')
    # print('initial',b)

    c=[]
    for i in b:
        temp=i+shift
        if temp>127:
            temp-=127
        c.append(temp)
    # print('list',c)
    return bytes(c).decode('ascii')
def decaesar(values,shift):
    b = values.encode(encoding='ascii')
    # print('initial',b)
    c = []
    for i in b:
        temp = i - shift
        if temp < 0:
            temp += 127
        c.append(temp)
    # print('list',c)
    return bytes(c).decode('ascii')

if __name__=='__main__':
    a=caesar(txt,sh)
    print(a)
    ua=decaesar(a,sh)
    print(ua)