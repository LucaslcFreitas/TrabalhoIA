from Arvore import Arvore
from NoArvore import NoArvore
import random


def executarOrdenada(barras):
    banana = False
    abismo = False

    # lista de abertos e fechados
    abertos = []
    fechados = []

    # cria ávore vazia, com a raíz sendo o macaco
    arvore = Arvore()
    abertos.append(arvore.getRaiz())

    # função auxiliar para reordanar a fila na ordem de custo real
    def __reordenaFila(fila):
        return sorted(fila, key=lambda no: no.getCustoAcumulado())

    while not banana and not abismo:
        if len(abertos) > 0:
            N = abertos.pop(0)

            if N.getNoLista().getFinal():
                banana = True
                __imprimeCaminhoSolução(N, abertos, fechados)
            else:
                if N.getNoLista().getNome() == "M":  # Regra R3
                    for i in range(0, 7):
                        novoNoArv = NoArvore(barras[i].getInicio(), N, False,
                                             barras[i].getInicio().getCustoReal())
                        N.addFilho(novoNoArv)
                        abertos.append(novoNoArv)
                else:  # Usar regras R1 e R2 alternadamente
                    if not N.getOpAnterior():  # Regra R1
                        if N.getNoLista().getProximo() != None:
                            novoNoArv = NoArvore(
                                N.getNoLista().getProximo(), N, True, N.getCustoAcumulado()+N.getNoLista().getProximo().getCustoReal())
                            N.addFilho(novoNoArv)
                            abertos.append(novoNoArv)
                    else:  # Regra R2
                        if N.getNoLista().getTroca() != None:
                            novoNoArv = NoArvore(
                                N.getNoLista().getTroca(), N, False, N.getCustoAcumulado()+N.getNoLista().getTroca().getCustoReal())
                            N.addFilho(novoNoArv)
                            abertos.append(novoNoArv)

                fechados.append(N)
                abertos = __reordenaFila(abertos)
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
        abertos.append(listaAbertos[i].getNoLista().getNome(
        )+"("+str(listaAbertos[i].getCustoAcumulado())+")")
    print("Lista de abertos: ", abertos)

    fechados = []
    for i in range(len(listaFechados)):
        fechados.append(listaFechados[i].getNoLista().getNome(
        )+"("+str(listaFechados[i].getCustoAcumulado())+")")
    print("Lista de fechados: ", fechados, "\n")
