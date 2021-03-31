import os

import kivy
from kivy.app import App
import psutil
from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanel
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem, TwoLineListItem

Builder.load_file('pong.kv')


class MyLayout(TabbedPanel):
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
                        TwoLineListItem(text = f'{arquivo}', secondary_text = f'{round(f_size, 2)} MB')
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


    # def on_start(self):
    #     for i in testandoLista:
    #         self.root.ids.panelArq.add_widget(
    #             OneLineListItem(text = f'{i}')
    #         )



if __name__== '__main__':
    AwesomeApp().run()


def arq():
    diretorio = input('informe um diretorio: ')
    nomeUsuario = os.getlogin()
    diretorio_vdd = f'C:\\Users\\{nomeUsuario}\\{diretorio}'
    lista_arquivos =[]
    try:
        arquivos = os.listdir(diretorio_vdd)
        for arquivo in arquivos:
            f_path = os.path.join(diretorio_vdd, arquivo)
            if os.path.isfile(f_path):
                f_size = os.path.getsize(f_path)
                lista_arquivos.append(arq)

    except FileNotFoundError as e:
        print(f'diretório não existe')
