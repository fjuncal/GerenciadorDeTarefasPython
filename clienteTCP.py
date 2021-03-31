import pickle
import socket

from pip._vendor.distlib.compat import raw_input

HOST = '127.0.0.1'     # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print('Para sair da conexão, basta digitar sair')
msg = raw_input()
while msg != 'sair':
    try:
        tcp.send(msg.encode('utf-8'))
        data = tcp.recv(1024)
        print(pickle.loads(data))
        msg = raw_input()
    except ConnectionResetError as e:
        print('Foi forçado um cancelamento da conexão com o servidor - Servidor offline')
        break
tcp.close()