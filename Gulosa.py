from Arvore import Arvore
from NoArvore import NoArvore
import random


def executarGulosa(barras):
    # lista de abertos e fechados
    abertos = []
    fechados = []

    sucesso = False
    fracasso = False

    # cria ávore vazia, somente com a raiz
    arvore = Arvore()
    abertos.append(arvore.getRaiz())

    # regras:
    #   R1: O macaco anda para cima.
    #   R2: O macaco troca para outra barra.
    #   R3: O macaco aponta para um dos nós Bi-1 onde i representa a barra vertical e varia de 0 a 6 e o 1 representa o primeiro nó.
    #
    # Obs: A regra R3 é utilizada para escolher a barra inicialmente e as regras R1 e R2 deve ser executadas alternadamente, pelo atributo opAnterior

    while not sucesso and not fracasso:
        if len(abertos) > 0:
            N = abertos.pop(0)

            if N.getNoLista().getFinal():
                sucesso = True
                __imprimeCaminhoSolução(N, abertos, fechados)
            else:
                if N.getNoLista().getNome() == "M":  # Regra R3
                    auxiliarRNG = []
                    while len(auxiliarRNG) < 7:
                        rng = random.randint(0, 6)
                        if rng not in auxiliarRNG:
                            novoNoArv = NoArvore(barras[rng].getInicio(), N, False)
                            N.addFilho(novoNoArv)
                            abertos.append(novoNoArv)
                            auxiliarRNG.append(rng)
                else:  # Usar regras R1 e R2
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
                abertos = __reordenaFila(abertos)
        else:
            fracasso = True

    if fracasso:
        print("Não foi possível encontrar a solução!")


def __reordenaFila(fila):
    return sorted(fila, key=lambda no: no.getNoLista().getHeuristica())


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
        abertos.append(listaAbertos[i].getNoLista().getNome(
        )+"("+str(listaAbertos[i].getNoLista().getHeuristica())+")")
    print("Lista de abertos: ", abertos)

    fechados = []
    for i in range(len(listaFechados)):
        fechados.append(listaFechados[i].getNoLista().getNome(
        )+"("+str(listaFechados[i].getNoLista().getHeuristica())+")")
    print("Lista de fechados: ", fechados, "\n")
