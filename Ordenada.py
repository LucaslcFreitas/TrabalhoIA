from Arvore import Arvore
from NoArvore import NoArvore
import random


def executarOrdenada(barras):
    # lista de abertos e fechados
    abertos = []
    fechados = []

    banana = False
    fracasso = False

    # cria árvore vazia, com a raiz sendo o macaco
    arvore = Arvore()
    abertos.append(arvore.getRaiz())

    iteracao = 0
    while not banana and not fracasso:
        iteracao = iteracao + 1
        if len(abertos) > 0:
            N = abertos.pop(0)

            if N.getNoLista().getFinal():
                banana = True
                __imprimeCaminhoSolução(N, iteracao, abertos, fechados)
            else:
                if N.getNoLista().getNome() == "M":  # Regra R1
                    for i in range(0, 7):
                        novoNoArv = NoArvore(barras[i].getInicio(), N, False,
                                             barras[i].getInicio().getCustoReal())
                        N.addFilho(novoNoArv)
                        abertos.append(novoNoArv)
                else:  # Usar regras R2 e R3 alternadamente
                    if not N.getOpAnterior():  # Regra R2
                        if N.getNoLista().getProximo() != None:
                            novoNoArv = NoArvore(
                                N.getNoLista().getProximo(), N, True, N.getCustoAcumulado()+N.getNoLista().getProximo().getCustoReal())
                            N.addFilho(novoNoArv)
                            abertos.append(novoNoArv)
                    else:  # Regra R3
                        if N.getNoLista().getTroca() != None:
                            novoNoArv = NoArvore(
                                N.getNoLista().getTroca(), N, False, N.getCustoAcumulado()+N.getNoLista().getTroca().getCustoReal())
                            N.addFilho(novoNoArv)
                            abertos.append(novoNoArv)

                fechados.append(N)

                # Iterações
                abertos = __printIteracaoEOrdenaLista(iteracao,
                                                      abertos, fechados)
        else:
            fracasso = True

    if fracasso:
        print("Nao foi possivel encontrar a solucao!")

# Função auxiliar para reordenar a fila na ordem de custo real


def __reordenaFila(fila):
    return sorted(fila, key=lambda no: no.getCustoAcumulado())


def __printIteracaoEOrdenaLista(iteracao, abertos, fechados):
    print(f"Iteracao: {iteracao}")

    __printLista("Fechados", fechados)
    __printLista("Abertos", abertos)
    abertos = __reordenaFila(abertos)
    __printLista("Ordenado", abertos)
    print("-------------------------")

    return abertos


def __imprimeCaminhoSolução(no, iteracoes, listaAbertos, listaFechados):
    print("Caminho encontrado!")
    print(f"Iteracoes: {iteracoes}")
    print("Custo real: ", no.getCustoAcumulado())

    caminho = []
    while no != None:
        caminho.append(no.getNoLista().getNome())
        no = no.getPai()
    caminho = caminho[::-1]
    print("Caminho solução: ", caminho)

    __printLista("Abertos", listaAbertos)
    __printLista("Fechados", listaFechados)


def __printLista(texto, lista):
    string = []
    for i in range(len(lista)):
        nome = lista[i].getNoLista().getNome()
        valor = lista[i].getCustoAcumulado()
        string.append(f"{nome}({valor})")
    print(f"{texto}: {string}")
