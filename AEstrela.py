from Arvore import Arvore
from NoArvore import NoArvore


def executarAEstrela(barras):
    abertos = []
    fechados = []

    # Cria árvore vazia, somente com a raiz
    # e adiciona a raiz na lista de abertos
    arvore = Arvore()
    abertos.append(arvore.getRaiz())

    # Regras:
    # R1: O macaco olha para um dos nós Bi-1 onde i representa a barra vertical e
    #     varia de 0 a 6 e o 1 representa o primeiro nó.
    # R2: O macaco anda para cima.
    # R3: O macaco troca para outra barra.
    #
    # Obs: A regra R1 é utilizada para escolher a barra inicialmente e as regras R2 e R3
    # deve ser executadas alternadamente, pelo atributo opAnterior

    iteracao = 0
    while True:
        iteracao = iteracao + 1
        if len(abertos) > 0:
            noAtual = abertos.pop(0)

            # Caso o No atual seja o que tem a banana
            if noAtual.getNoLista().getFinal():
                __imprimeCaminhoSolucao(noAtual, iteracao, abertos, fechados)
                break
            else:
                if noAtual.getNoLista().getNome() == "M":  # Regra R1

                    for i in range(0, 7):
                        novoNoArv = NoArvore(barras[i].getInicio(), noAtual,
                                             False, barras[i].getInicio().getCustoReal())

                        noAtual.addFilho(novoNoArv)
                        abertos.append(novoNoArv)

                else:  # Usar regras R2 e R3
                    if not noAtual.getOpAnterior():  # Regra R2
                        proximoNo = noAtual.getNoLista().getProximo()
                        if proximoNo != None:
                            custoAcumulado = (noAtual.getCustoAcumulado() +
                                              proximoNo.getCustoReal())

                            novoNoArv = NoArvore(proximoNo, noAtual,
                                                 True, custoAcumulado)
                            noAtual.addFilho(novoNoArv)
                            abertos.append(novoNoArv)
                    else:  # Regra R3
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
                abertos = __printIteracaoEOrdenaLista(iteracao,
                                                      abertos, fechados)
        else:
            print("Nao foi possivel encontrar a solucao!")
            break


def __reordenaListaAbertos(abertos):
    return sorted(abertos, key=lambda noArv: noArv.getSomaCustoAcumuladoHeuristica())


def __imprimeCaminhoSolucao(no, iteracoes, listaAbertos, listaFechados):
    print("Caminho encontrado!")
    print(f"Iteracoes: {iteracoes}")
    print("Custo real: ", no.getCustoAcumulado())

    caminho = []
    while no != None:
        caminho.append(no.getNoLista().getNome())
        no = no.getPai()

    caminho = caminho[::-1]
    print(f"Solucao: {caminho}")

    __printLista("Abertos", listaAbertos)
    __printLista("Fechados", listaFechados)


def __printIteracaoEOrdenaLista(iteracao, abertos, fechados):
    print(f"Iteracao: {iteracao}")

    __printLista("Fechados", fechados)
    __printLista("Abertos", abertos)
    abertos = __reordenaListaAbertos(abertos)
    __printLista("Ordenado", abertos)
    print("-------------------------")

    return abertos


def __printLista(texto, lista):
    string = []
    for i in range(len(lista)):
        nome = lista[i].getNoLista().getNome()
        valor = lista[i].getSomaCustoAcumuladoHeuristica()
        string.append(f"{nome}({valor})")
    print(f"{texto}: {string}")
