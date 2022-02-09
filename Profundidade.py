from Arvore import Arvore
from NoArvore import NoArvore
from ImprimeArvore import imprimeArvore


def executarProfundidade(barras):
    banana = False
    fracasso = False

    # Pilha de abertos
    abertos = []
    fechados = []

    # Cria árvore vazia, com a raiz sendo o macaco
    arvore = Arvore()
    abertos.append(arvore.getRaiz())
    cont = 0

    iteracao = 0
    while not banana and not fracasso:
        iteracao = iteracao + 1
        if len(abertos) > 0:
            N = abertos[len(abertos)-1]

            if N.getNoLista().getFinal():
                banana = True
                __imprimeCaminhoSolução(N, iteracao, abertos, fechados)
                imprimeArvore(arvore.getRaiz(), "Profundidade")
            else:
                if N.getNoLista().getNome() == "M":  # Regra R1
                    novoNoArv = NoArvore(barras[cont].getInicio(), N, False)
                    N.addFilho(novoNoArv)
                    if cont == 7:
                        abertos.pop()
                    abertos.append(novoNoArv)
                    cont = cont + 1
                    __printIteracao(iteracao, abertos, fechados)
                else:  # Usar regras R2 e R3 alternadamente
                    abertos.pop()
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
                    __printIteracao(iteracao, abertos, fechados)
        else:
            fracasso = True

    if fracasso:
        print("Nao foi possivel encontrar a solucao!")


def __printIteracao(iteracao, abertos, fechados):
    print(f"Iteracao: {iteracao}")

    __printLista("Fechados", fechados)
    __printLista("Abertos", abertos)
    print("-------------------------")

    return abertos


def __imprimeCaminhoSolução(no, iteracoes, listaAbertos, listaFechados):
    print("Caminho encontrado!")
    print(f"Iteracoes: {iteracoes}")

    caminho = []
    while no != None:
        caminho.append(no.getNoLista().getNome())
        no = no.getPai()

    caminho = caminho[::-1]
    print("Solução: ", caminho)

    __printLista("Abertos", listaAbertos)
    __printLista("Fechados", listaFechados)


def __printLista(texto, lista):
    string = []
    for i in range(len(lista)):
        nome = lista[i].getNoLista().getNome()
        string.append(f"{nome}")
    print(f"{texto}: {string}")
