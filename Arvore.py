from NoArvore import NoArvore
from NoLista import NoLista


class Arvore(object):
    __raiz = None

    def __init__(self):
        self.__raiz = NoArvore(NoLista("M"), None, True)

    def getRaiz(self) -> NoArvore:
        return self.__raiz
