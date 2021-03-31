import os, cpuinfo

import psutil
from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanel
from kivymd.app import MDApp
import socket
import pickle
from pip._vendor.distlib.compat import raw_input

from kivymd.uix.list import TwoLineListItem


Builder.load_file('pong.kv')


class MyLayout(TabbedPanel):
    # def ligarCliente(self):
    #     HOST = '127.0.0.1'  # Endereco IP do Servidor
    #     PORT = 5000  # Porta que o Servidor esta
    #     tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     dest = (HOST, PORT)
    #     tcp.connect(dest)
    #     print('Para sair da conexão, basta digitar sair')
    #     msg = raw_input()
    #     while msg != 'sair':
    #         try:
    #             tcp.send(msg.encode('utf-8'))
    #             data = tcp.recv(1024)
    #             print(pickle.loads(data))
    #             msg = raw_input()
    #         except ConnectionResetError as e:
    #             print('Foi forçado um cancelamento da conexão com o servidor - Servidor offline')
    #             break
    #     tcp.close()
    #
    # def ligarServidor(self):
    #     HOST = ''  # Endereco IP do Servidor
    #     PORT = 5000  # Porta que o Servidor esta
    #     tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #     orig = (HOST, PORT)
    #     tcp.bind(orig)
    #     tcp.listen(1)
    #
    #     nomeUsuario = os.getlogin()
    #     while True:
    #         con, cliente = tcp.accept()
    #         print('Concetado por', cliente)
    #         while True:
    #             try:
    #                 msg = con.recv(1024).decode()
    #             except ConnectionResetError as e:
    #                 print(f'Cliente: {cliente[0]} desconectou!')
    #                 break
    #             if not msg: break
    #             diretorio_vdd = f'C:\\Users\\{nomeUsuario}\\{msg}'
    #             try:
    #                 listaArq = os.listdir(diretorio_vdd)
    #                 bytes_resp = pickle.dumps(listaArq)
    #                 print(listaArq)
    #                 con.sendall(bytes_resp)
    #             except FileNotFoundError as e:
    #                 msg_erro = 'diretório não existe'
    #                 print(msg_erro)
    #                 bytes_resp_erro = pickle.dumps(msg_erro)
    #                 con.sendall(bytes_resp_erro)
    #         print('Finalizando conexao do cliente', cliente)
    #         con.close()

    def calculaCPU(self):
        self.ids.label_porcentagemCPU.text = ''
        self.ids.progressBar_cpuPorcentagem.value = 0

        cpuPorcentagem = psutil.cpu_percent(interval=0)
        self.ids.label_porcentagemCPU.text = f'{cpuPorcentagem} %'
        self.ids.progressBar_cpuPorcentagem.value = cpuPorcentagem

    def calculaMemoria(self):
        self.ids.label_qtdTotal.text = ''
        self.ids.label_qtdSendoUsada.text = ''
        self.ids.label_porcentagemUsada.text = ''
        self.ids.progressBar_porcentagem.value = 0

        memoriaTotal = psutil.virtual_memory().total
        convertendoTotal = memoriaTotal / (1024.0 ** 3)
        self.ids.label_qtdTotal.text = f'{round(convertendoTotal, 2)} GB'

        memoriaSendoUsada = psutil.virtual_memory().used
        convertendoUsada = memoriaSendoUsada / (1024.0 ** 3)
        self.ids.label_qtdSendoUsada.text = f'{round(convertendoUsada, 2)} GB'

        porcentagemUsada = psutil.virtual_memory().percent
        convertendoPorcentagem = round(porcentagemUsada, 2)
        self.ids.label_porcentagemUsada.text = f'{convertendoPorcentagem} %'
        self.ids.progressBar_porcentagem.value = convertendoPorcentagem


    def pegarArq(self):
        self.ids.panelArq.clear_widgets()
        diretorio = self.ids.text_field_arquivo.text
        nomeUsuario = os.getlogin()
        diretorio_vdd = f'C:\\Users\\{nomeUsuario}\\{diretorio}'
        try:
            arquivos = os.listdir(diretorio_vdd)
            for arquivo in arquivos:
                f_path = os.path.join(diretorio_vdd, arquivo)
                if os.path.isfile(f_path):
                    f_size = os.path.getsize(f_path)  / (1024.0 ** 2)
                    self.ids.panelArq.add_widget(
                        TwoLineListItem(text = f'{arquivo}', secondary_text = f'{round(f_size, 2)} MB', on_press = lambda x: print(f'Arquivo: {x.text} | Tamanho: {x.secondary_text}'))
                    )

        except FileNotFoundError as e:
            print(f'diretório não existe')
        self.ids.text_field_arquivo.text = ''


class AwesomeApp(MDApp):
    def build(self):
        return MyLayout()

    def on_start(self):
        memoriaTotal = psutil.virtual_memory().total
        convertendoTotal = memoriaTotal / (1024.0 ** 3)
        self.root.ids.label_qtdTotal.text = f'{round(convertendoTotal, 2)} GB'

        memoriaSendoUsada = psutil.virtual_memory().used
        convertendoUsada = memoriaSendoUsada / (1024.0 ** 3)
        self.root.ids.label_qtdSendoUsada.text = f'{round(convertendoUsada, 2)} GB'

        porcentagemUsada = psutil.virtual_memory().percent
        convertendoPorcentagem = round(porcentagemUsada, 2)
        self.root.ids.label_porcentagemUsada.text = f'{convertendoPorcentagem} %'
        self.root.ids.progressBar_porcentagem.value = convertendoPorcentagem

        info_cpu = cpuinfo.get_cpu_info()
        cpuMarca = info_cpu['brand_raw']
        cpuArquitetura = info_cpu['arch']
        cpuBits = info_cpu['bits']
        cpuNucleos = os.cpu_count()
        cpuPorcentagem = psutil.cpu_percent(interval=0)

        self.root.ids.label_nomeCPU.text = f'{cpuMarca}'
        self.root.ids.label_arquiteturaCPU.text = f'{cpuArquitetura}'
        self.root.ids.label_bitsCPU.text = f'{cpuBits} bits'
        self.root.ids.label_nucleosCPU.text = f'{cpuNucleos} núcleos'
        self.root.ids.label_porcentagemCPU.text = f'{cpuPorcentagem} %'
        self.root.ids.progressBar_cpuPorcentagem.value = cpuPorcentagem

        disco = psutil.disk_usage('.')
        discoTotal = disco.total / (1024.0 ** 3)
        discoSendoUsado = disco.used / (1024.0 ** 3)
        discoEspacoLivre = disco.free / (1024.0 ** 3)
        discoPorcentagem = disco.percent

        self.root.ids.label_quantidadeTotalDisco.text = f'{round(discoTotal, 2)} GB'
        self.root.ids.label_qtdSendoUsadaDisco.text = f'{round(discoSendoUsado, 2)} GB'
        self.root.ids.label_qtdLivreDisco.text = f'{round(discoEspacoLivre, 2)} GB'
        self.root.ids.label_porcentagemDisco.text = f'{round(discoPorcentagem, 2)} %'
        self.root.ids.progressBar_discoPorcentagem.value = discoPorcentagem

        for proc in psutil.process_iter():
            info = proc.as_dict(attrs=['pid', 'name'])
            self.root.ids.listaProcessos.add_widget(
                TwoLineListItem(text=f'{info["name"]}', secondary_text=f'PID - {info["pid"]}',  on_press = lambda x: print(f'Processo: {x.text} | {x.secondary_text}'))
            )
        hostname = socket.gethostname()
        IP = socket.gethostbyname(hostname)
        self.root.ids.label_ip.text = f'{IP}'


if __name__== '__main__':
    AwesomeApp().run()


