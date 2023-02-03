import socket
from caesar import caesar,decaesar
sh=90
serv_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serv_sock.bind(('localhost',55555))
serv_sock.listen(10)
print('server started')
client_sock, client_addr=serv_sock.accept()
print(f'accept connection: {client_addr}')
leter= caesar( 'hello ,client. do u want to continue(y/n)?',sh)
client_sock.sendall(leter.encode('ascii'))
terminator =True if decaesar(client_sock.recv(1024).decode('ascii'),sh)=='y' else False

while terminator:
    leter = caesar('enter operator +,-,*,/,**', sh)
    client_sock.sendall(leter.encode('ascii'))
    operation=decaesar(client_sock.recv(1024).decode('ascii'),sh)
    print('operator: ',operation)

    leter = caesar('enter left value', sh)
    client_sock.sendall(leter.encode('ascii'))
    l_value=decaesar(client_sock.recv(1024).decode('ascii'),sh)
    print('left value: ',l_value)

    leter = caesar('enter right value', sh)
    client_sock.sendall(leter.encode('ascii'))
    r_value=decaesar(client_sock.recv(1024).decode('ascii'),sh)
    print('right value: ',r_value)

    if operation=='+':
        txt=caesar(str(int(l_value)+int(r_value))+'\n',sh)
        client_sock.sendall(txt.encode('ascii'))

    elif operation=='-':
        txt=caesar(str(int(l_value)-int(r_value))+'\n',sh)
        client_sock.sendall(txt.encode('ascii'))

    elif operation=='*':
        txt=caesar(str(int(l_value)*int(r_value))+'\n',sh)
        client_sock.sendall(txt.encode('ascii'))

    elif operation=='/':
        txt=caesar(str(int(l_value)/int(r_value))+'\n',sh)
        client_sock.sendall(txt.encode('ascii'))

    elif operation=='**':
        txt=caesar(str(int(l_value)**int(r_value))+'\n',sh)
        client_sock.sendall(txt.encode('ascii'))

    if not operation:
        break

serv_sock.close()