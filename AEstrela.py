from io import BufferedRandom
from Arvore import Arvore
from NoArvore import NoArvore


def executarAEstrela(barras):
    abertos = []
    fechados = []
    f = open("./resultados/AEstrela.txt", "w")
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
                __imprimeCaminhoSolução(f, noAtual, abertos, fechados)
                break
            else:
                if noAtual.getNoLista().getNome() == "M":  # Regra R3

                    for i in range(0, 7):
                        novoNoArv = NoArvore(barras[i].getInicio(), noAtual,
                                             False, barras[i].getInicio().getCustoReal())

                        noAtual.addFilho(novoNoArv)
                        abertos.append(novoNoArv)

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
                abertos = __printIteracaoEOrdenaLista(iteracao,
                                                      f, abertos, fechados)
        else:
            print("Não foi possível encontrar a solução!")
            break
    f.close()


def __reordenaListaAbertos(abertos):
    return sorted(abertos, key=lambda noArv: noArv.getSomaCustoAcumuladoHeuristica())


def __imprimeCaminhoSolução(f: BufferedRandom, no, listaAbertos, listaFechados):
    print("Caminho encontrado!")
    f.write("Caminho encontrado!\n")

    caminho = []
    while no != None:
        caminho.append(no.getNoLista().getNome())
        no = no.getPai()

    caminho = caminho[::-1]
    print(f"Solucao: {caminho}")
    f.write(f"Solucao: {caminho}\n")

    __printLista(f, "Abertos", listaAbertos)
    __printLista(f, "Fechados", listaFechados)


def __printIteracaoEOrdenaLista(iteracao, file: BufferedRandom, abertos, fechados):
    print(f"Iteracao: {iteracao}")
    file.write(f"Iteracao: {iteracao} \n")
    __printLista(file, "Fechados", fechados)
    __printLista(file, "Abertos", abertos)
    abertos = __reordenaListaAbertos(abertos)
    __printLista(file, "Ordenado", abertos)
    print("-------------------------")
    file.write("-------------------------\n")
    return abertos


def __printLista(file: BufferedRandom, texto, lista):
    string = []
    for i in range(len(lista)):
        nome = lista[i].getNoLista().getNome()
        valor = lista[i].getSomaCustoAcumuladoHeuristica()
        string.append(f"{nome}({valor})")
    print(f"{texto}: {string}")
    file.write(f"{texto}: {string} \n")
