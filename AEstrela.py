from Arvore import Arvore
from NoArvore import NoArvore
import random


def executarAEstrela(barras):
    abertos = []
    fechados = []

    # cria árvore vazia, somente com a raiz
    # e adiciona a raiz na lista de abertos
    arvore = Arvore()
    abertos.append(arvore.getRaiz())

    # regras:
    #   R1: O macaco anda para cima.
    #   R2: O macaco troca para outra barra.
    #   R3: O macaco aponta para um dos nós Bi-1 onde i representa a
    #       barra vertical e varia de 0 a 6 e o 1 representa o primeiro nó.
    #
    # Obs: A regra R3 é utilizada para escolher a barra
    # inicialmente e as regras R1 e R2 deve ser executadas alternadamente, pelo atributo opAnterior

    iteracao = 0
    while True:
        iteracao = iteracao + 1
        if len(abertos) > 0:
            noAtual = abertos.pop(0)

            # Caso o No atual seja o que tem a banana
            if noAtual.getNoLista().getFinal():
                __imprimeCaminhoSolução(noAtual, abertos, fechados)
                break
            else:
                if noAtual.getNoLista().getNome() == "M":  # Regra R3
                    auxiliarRNG = []
                    while len(auxiliarRNG) < 7:
                        rng = random.randint(0, 6)
                        if rng not in auxiliarRNG:

                            novoNoArv = NoArvore(
                                barras[rng].getInicio(), noAtual, False, barras[rng].getInicio(
                                ).getCustoReal())

                            noAtual.addFilho(novoNoArv)
                            abertos.append(novoNoArv)
                            auxiliarRNG.append(rng)
                else:  # Usar regras R1 e R2
                    if not noAtual.getOpAnterior():  # Regra R1
                        proximoNo = noAtual.getNoLista().getProximo()
                        if proximoNo != None:
                            custoAcumulado = (noAtual.getCustoAcumulado() +
                                              proximoNo.getCustoReal())

                            novoNoArv = NoArvore(
                                proximoNo, noAtual, True, custoAcumulado)
                            noAtual.addFilho(novoNoArv)
                            abertos.append(novoNoArv)
                    else:  # Regra R2
                        trocaNo = noAtual.getNoLista().getTroca()
                        if trocaNo != None:
                            custoAcumulado = (noAtual.getCustoAcumulado() +
                                              trocaNo.getCustoReal())
                            novoNoArv = NoArvore(
                                trocaNo, noAtual, False, custoAcumulado)
                            noAtual.addFilho(novoNoArv)
                            abertos.append(novoNoArv)
                fechados.append(noAtual)

                # Iterações
                print("Iteracao: ", iteracao)
                printArray("Fechados", fechados)
                printArray("Abertos", abertos)
                abertos = __reordenaListaAbertos(abertos)
                printArray("Ordenado", abertos)
                print("-------------------------")
        else:
            print("Não foi possível encontrar a solução!")
            break


def __reordenaListaAbertos(abertos):
    return sorted(abertos, key=lambda noArv: noArv.getSomaCustoAcumuladoHeuristica())


def __imprimeCaminhoSolução(no, listaAbertos, listaFechados):
    print("Caminho encontrado!")
    caminho = []
    somaCustoReal = 0
    somaCustoHeuristica = 0
    while no != None:
        somaCustoReal = somaCustoReal + no.getNoLista().getCustoReal()
        somaCustoHeuristica = somaCustoHeuristica + no.getNoLista().getHeuristica()
        caminho.append(no.getNoLista().getNome())
        no = no.getPai()

    caminho = caminho[::-1]
    print("Caminho solução: ", caminho)
    print("Custo Real: ", somaCustoReal)
    print("Custo Heuristica: ", somaCustoHeuristica)

    abertos = []
    for i in range(len(listaAbertos)):
        nome = listaAbertos[i].getNoLista().getNome()
        valor = listaAbertos[i].getSomaCustoAcumuladoHeuristica()
        abertos.append(f"{nome}({valor})")

    print("Lista de abertos: ", abertos)

    fechados = []
    for i in range(len(listaFechados)):
        nome = listaFechados[i].getNoLista().getNome()
        valor = listaFechados[i].getSomaCustoAcumuladoHeuristica()
        fechados.append(f"{nome}({valor})")

    print("Lista de fechados: ", fechados, "\n")


def printArray(texto, lista):
    string = []
    for i in range(len(lista)):
        nome = lista[i].getNoLista().getNome()
        valor = lista[i].getSomaCustoAcumuladoHeuristica()
        string.append(f"{nome}({valor})")
    print(f"{texto}: {string}")
