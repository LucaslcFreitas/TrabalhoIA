import ctypes
from NoLista import NoLista


class NoArvore(object):
    __pai = None
    __noLista = None
    __filhos = None
    # Define se a operação anterior foi subir ou troca. True = subir, False troca
    __opAnterior = None
    __custoAcumulado = None  # Utilizado na busca A*

    def __init__(self, noLista, pai, opAterior, custoAcumulado=None) -> None:
        self.__pai = pai
        self.__noLista = noLista
        self.__filhos = []
        self.__opAnterior = opAterior
        self.__custoAcumulado = custoAcumulado

    def addFilho(self, filho) -> None:
        self.__filhos.append(filho)

    def getPai(self) -> NoLista:
        return self.__pai

    def getNoLista(self) -> NoLista:
        return self.__noLista

    def getFilhos(self) -> ctypes.Array:
        return self.__filhos

    def getOpAnterior(self) -> bool:
        return self.__opAnterior

    def getCustoAcumulado(self) -> int:
        return self.__custoAcumulado
