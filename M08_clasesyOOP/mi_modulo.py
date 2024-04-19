import sys
sys.path.append(r"/home/rafa/Documentos/Henry/Python-Prep/M07_funciones")
from Prep_Course_Homework_07_Resuelto import verifica_primo, valor_modal, conversion_grados, factorial


class Funciones_utiles ():
    def __init__(self,lista):
        self.lista = lista

    def verifica_primo (self):
        for elemento in self.lista:
            print(elemento, verifica_primo(elemento))
    
    def valor_modal (self):
        print(valor_modal(self.lista))
    
    def conversion_grados (self, origen, destino):
        for elemento in self.lista:
            print('Origen:',elemento,' Destino:',conversion_grados (elemento, origen, destino))
    
    def factorial (self):
        for elemento in self.lista:
            print(factorial(elemento))