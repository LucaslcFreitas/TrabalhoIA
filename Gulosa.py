from Arvore import Arvore
from NoArvore import NoArvore


def executarGulosa(barras):
    # Lista de abertos e fechados
    abertos = []
    fechados = []

    sucesso = False
    fracasso = False

    # Cria árvore vazia, somente com a raiz
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
    while not sucesso and not fracasso:
        iteracao = iteracao + 1
        if len(abertos) > 0:
            N = abertos.pop(0)

            if N.getNoLista().getFinal():
                sucesso = True
                __imprimeCaminhoSolucao(N, iteracao, abertos, fechados)
            else:
                if N.getNoLista().getNome() == "M":  # Regra R1
                    for i in range(0, 7):
                        novoNoArv = NoArvore(barras[i].getInicio(), N, False)
                        N.addFilho(novoNoArv)
                        abertos.append(novoNoArv)

                else:  # Usar regras R2 e R3
                    if not N.getOpAnterior():  # Regra R2
                        if N.getNoLista().getProximo() != None:
                            novoNoArv = NoArvore(N.getNoLista().getProximo(),
                                                 N, True)
                            N.addFilho(novoNoArv)
                            abertos.append(novoNoArv)
                    else:  # Regra R3
                        if N.getNoLista().getTroca() != None:
                            novoNoArv = NoArvore(N.getNoLista().getTroca(),
                                                 N, False)
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


def __reordenaFila(fila):
    return sorted(fila, key=lambda no: no.getNoLista().getHeuristica())


def __printIteracaoEOrdenaLista(iteracao, abertos, fechados):
    print(f"Iteracao: {iteracao}")

    __printLista("Fechados", fechados)
    __printLista("Abertos", abertos)
    abertos = __reordenaFila(abertos)
    __printLista("Ordenado", abertos)
    print("-------------------------")

    return abertos


def __imprimeCaminhoSolucao(no, iteracoes, listaAbertos, listaFechados):
    print("Caminho encontrado!")
    print(f"Iteracoes: {iteracoes}")

    caminho = []
    while no != None:
        caminho.append(no.getNoLista().getNome())
        no = no.getPai()

    caminho = caminho[::-1]
    print(f"Solucao: {caminho}")

    __printLista("Abertos", listaAbertos)
    __printLista("Fechados", listaFechados)


def __printLista(texto, lista):
    string = []
    for i in range(len(lista)):
        nome = lista[i].getNoLista().getNome()
        valor = lista[i].getNoLista().getHeuristica()
        string.append(f"{nome}({valor})")
    print(f"{texto}: {string}")
