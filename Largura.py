from Arvore import Arvore
from NoArvore import NoArvore
from ImprimeArvore import imprimeArvore


def executarLargura(barras):
    # lista de abertos e fechados
    abertos = []
    fechados = []
    banana = False
    fracasso = False

    # Cria árvore vazia, com a raiz sendo o macaco
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
                imprimeArvore(arvore.getRaiz(), "Largura")
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

                # Iterações
                __printIteracao(iteracao, abertos, fechados)

        else:
            fracasso = True
        if fracasso:
            print("Não foi possível encontrar a solução!")


def __imprimeCaminhoSolução(no, iteracoes, listaAbertos, listaFechados):
    print("Caminho encontrado!")
    print(f"Iteracoes: {iteracoes}")

    caminho = []
    while no != None:
        caminho.append(no.getNoLista().getNome())
        no = no.getPai()
    caminho = caminho[::-1]
    print("Solucao: ", caminho)

    __printLista("Abertos", listaAbertos)
    __printLista("Fechados", listaFechados)


def __printIteracao(iteracao, abertos, fechados):
    print(f"Iteracao: {iteracao}")

    __printLista("Fechados", fechados)
    __printLista("Abertos", abertos)
    print("-------------------------")


def __printLista(texto, lista):
    string = []
    for i in range(len(lista)):
        nome = lista[i].getNoLista().getNome()
        string.append(f"{nome}")
    print(f"{texto}: {string}")
