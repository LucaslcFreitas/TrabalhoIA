from Arvore import Arvore
from NoArvore import NoArvore
import random


def executarProfundidade(barras):
    banana = False
    abismo = False

    # lista de abertos e fechados
    abertos = []
    fechados = []

    # cria ávore vazia, com a raíz sendo o macaco
    arvore = Arvore()
    abertos.append(arvore.getRaiz())
    cont = 0

    while not banana and not abismo:
        if len(abertos) > 0:
            N = abertos[len(abertos)-1]

            if N.getNoLista().getFinal():
                banana = True
                __imprimeCaminhoSolução(N, abertos, fechados)
            else:
                if N.getNoLista().getNome() == "M":  # Regra R3
                    auxiliar = []
                    novoNoArv = NoArvore(barras[cont].getInicio(), N, False)
                    N.addFilho(novoNoArv)
                    auxiliar.append(cont)
                    if len(auxiliar) == 7:
                        abertos.pop()
                    abertos.append(novoNoArv)
                    cont = cont + 1

                else:  # Usar regras R1 e R2 alternadamente
                    abertos.pop()
                    if not N.getOpAnterior():  # Regra R1
                        if N.getNoLista().getProximo() != None:
                            novoNoArv = NoArvore(
                                N.getNoLista().getProximo(), N, True)
                            N.addFilho(novoNoArv)
                            abertos.append(novoNoArv)
                    else:  # Regra R2
                        if N.getNoLista().getTroca() != None:
                            novoNoArv = NoArvore(
                                N.getNoLista().getTroca(), N, False)
                            N.addFilho(novoNoArv)
                            abertos.append(novoNoArv)

                    fechados.append(N)
        else:
            abismo = True

    if abismo:
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
