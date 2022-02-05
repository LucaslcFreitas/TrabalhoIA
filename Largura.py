from Arvore import Arvore
from NoArvore import NoArvore
import random


def executarLargura(barras):
    # lista de abertos e fechados
    abertos = []
    fechados = []
    banana = False
    fracasso = False

    # cria ávore vazia, com a raíz sendo o macaco
    arvore = Arvore()
    abertos.append(arvore.getRaiz())

    while not banana and not fracasso:
        if len(abertos) > 0:
            N = abertos.pop(0)

            if N.getNoLista().getFinal():
                banana = True
                __imprimeCaminhoSolução(N, abertos, fechados)

            else:
                if N.getNoLista().getNome() == "M":  # Faz o macaco escolher uma barra da esquerda para a direita
                    for i in range(0, 7):
                        novoNoArv = NoArvore(barras[i].getInicio(), N, False)
                        N.addFilho(novoNoArv)
                        abertos.append(novoNoArv)

                else:  # Movimentações do macaco
                    if not N.getOpAnterior():  # Se o macaco ainda nao andou pra cima
                        if N.getNoLista().getProximo() != None:
                            novoNoArv = NoArvore(
                                N.getNoLista().getProximo(), N, True)
                            N.addFilho(novoNoArv)
                            abertos.append(novoNoArv)
                    else:  # Troca de barra
                        if N.getNoLista().getTroca() != None:
                            novoNoArv = NoArvore(
                                N.getNoLista().getTroca(), N, False)
                            N.addFilho(novoNoArv)
                            abertos.append(novoNoArv)
                fechados.append(N)
        else:
            fracasso = True
        if fracasso:
            print("Não foi possível encontrar a solução!")


def __imprimeCaminhoSolução(no, listaAbertos, listaFechados):
    print("Caminho encontrado!")
    caminho = []
    while no != None:
        caminho.append(no.getNoLista().getNome())
        no = no.getPai()
    caminho = caminho[::-1]
    print("Caminho solução: ", caminho)

    abertos = []
    for i in range(len(listaAbertos)):
        abertos.append(listaAbertos[i].getNoLista().getNome())
    print("Lista de abertos: ", abertos)

    fechados = []
    for i in range(len(listaFechados)):
        fechados.append(listaFechados[i].getNoLista().getNome())
    print("Lista de fechados: ", fechados, "\n")
