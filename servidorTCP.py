import pickle
import socket
import os


HOST = ''              # Endereco IP do Servidor
PORT = 5000            # Porta que o Servidor esta
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)

nomeUsuario = os.getlogin()
while True:
    con, cliente = tcp.accept()
    print('Concetado por', cliente)
    while True:
        try:
            msg = con.recv(1024).decode()
        except ConnectionResetError as e:
            print(f'Cliente: {cliente[0]} desconectou!')
            break
        if not msg: break
        diretorio_vdd = f'C:\\Users\\{nomeUsuario}\\{msg}'
        try:
            listaArq = os.listdir(diretorio_vdd)
            bytes_resp = pickle.dumps(listaArq)
            print(listaArq)
            con.sendall(bytes_resp)
        except FileNotFoundError as e:
            msg_erro = 'diretório não existe'
            print(msg_erro)
            bytes_resp_erro = pickle.dumps(msg_erro)
            con.sendall(bytes_resp_erro)
    print('Finalizando conexao do cliente', cliente)
    con.close()