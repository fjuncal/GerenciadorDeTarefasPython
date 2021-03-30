import os

import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanel
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem, TwoLineListItem

Builder.load_file('pong.kv')


class MyLayout(TabbedPanel):

    def pegarArq(self):
        diretorio = self.ids.text_field_arquivo.text
        nomeUsuario = os.getlogin()
        diretorio_vdd = f'C:\\Users\\{nomeUsuario}\\{diretorio}'
        try:
            arquivos = os.listdir(diretorio_vdd)
            for arquivo in arquivos:
                f_path = os.path.join(diretorio_vdd, arquivo)
                if os.path.isfile(f_path):
                    f_size = os.path.getsize(f_path)
                    self.ids.panelArq.add_widget(
                        TwoLineListItem(text = f'{arquivo}', secondary_text = f'{round(f_size, 2)}    Bytes')
                    )

        except FileNotFoundError as e:
            print(f'diretório não existe')
        self.ids.text_field_arquivo.text = ''


class AwesomeApp(MDApp):
    def build(self):
        return MyLayout()

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
