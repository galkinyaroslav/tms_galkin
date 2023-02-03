import socket
from caesar import caesar,decaesar
sh=90
client_sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client_sock.connect(('localhost',55555))
# client_sock.sendall('Hello'.encode('ascii'))
initial_data = decaesar(client_sock.recv(1024).decode("ascii"),sh)
print(f'initial_data: {initial_data}')
data_to_send = input('To send: ')
client_sock.sendall(caesar(data_to_send,sh).encode('ascii'))

# terminator=True
while True:
    received_data = decaesar(client_sock.recv(1024).decode("ascii"),sh)
    print(f'Received: {received_data}')
    data_to_send = input('To send: ')
    if data_to_send=='exit':
        break
    client_sock.sendall(caesar(data_to_send,sh).encode('ascii'))




client_sock.close()