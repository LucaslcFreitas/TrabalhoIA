from numpy import integer
from No import No


class ListaEncad(object):
    __inicio = None
    __tamanho = 0

    def __init__(self):
        self.__inicio = None
        self.__tamanho = 0

    def getInicio(self) -> No:
        return self.__inicio

    def getTamanho(self) -> integer:
        return self.__tamanho

    def adicionaFinal(self, no: No):
        if self.__inicio == None:
            self.__inicio = no
        else:
            noAtual = self.__inicio.getProximo()
            noAnterior = self.__inicio
            while noAtual != None:
                noAnterior = noAtual
                noAtual = noAtual.getProximo()
            noAnterior.setProximo(no)
        self.__tamanho = self.__tamanho + 1

    def getIndice(self, indice: int) -> No:
        cont = 0
        noAtual = self.__inicio

        while noAtual != None and indice != cont:
            cont = cont + 1
            noAtual = noAtual.getProximo()

        if cont == indice:
            return noAtual
        else:
            return None
