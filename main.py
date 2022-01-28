import random
from ListaEncad import ListaEncad
from NoLista import NoLista
from Largura import executarLargura
from Profundidade import executarProfundidade
from Ordenada import executarOrdenada
from Gulosa import executarGulosa
from AEstrela import executarAEstrela

barras = []


def interface():
    print("\nMENU")

    print("1 - Busca em Largura")
    print("2 - Busca em Profundidade")
    print("3 - Busca Ordenada")
    print("4 - Busca Gulosa")
    print("5 - Busca A*")
    print("0 - Sair")


def main():
    preencheListaEncad()
    interface()

    while True:
        entrada = input()

        # Busca em Largura
        if entrada == "1":
            print("Implementação da busca em largura")
            executarLargura(barras)
        elif entrada == "2":
            print("Implementação da busca em profundidade")
            executarProfundidade(barras)
        elif entrada == "3":
            print("Implementação da busca ordenada")
            executarOrdenada(barras)
        elif entrada == "4":
            print("Implementação da busca gulosa")
            executarGulosa(barras)
        elif entrada == "5":
            print("Implementação da busca A*")
            executarAEstrela(barras)
        elif entrada == "0":
            break
        else:
            print("Opção Inválida")


def preencheListaEncad():
    # cria as listas sem transições horizontais
    qtBarrasNos = [7, 13, 14, 11, 6, 7, 6]

    for i in range(7):
        aux = ListaEncad()
        for j in range(qtBarrasNos[i]):
            aux.adicionaFinal(NoLista("B"+str(i+1)+"-"+str(j+1)))
        barras.append(aux)

    # Adiciona as transições horizontais
    transicaoLateral(0, 1, 1, 1)
    transicaoLateral(0, 2, 1, 2)
    transicaoLateral(0, 3, 1, 3)
    transicaoLateral(0, 4, 1, 5)
    transicaoLateral(0, 5, 1, 6)
    transicaoLateral(0, 6, 1, 10)
    transicaoLateral(1, 4, 2, 3)
    transicaoLateral(1, 7, 2, 8)
    transicaoLateral(1, 8, 2, 9)
    transicaoLateral(1, 9, 2, 11)
    transicaoLateral(1, 11, 2, 12)
    transicaoLateral(1, 12, 2, 13)
    transicaoLateral(2, 1, 3, 1)
    transicaoLateral(2, 2, 3, 2)
    transicaoLateral(2, 4, 3, 4)
    transicaoLateral(2, 5, 3, 5)
    transicaoLateral(2, 6, 3, 6)
    transicaoLateral(2, 7, 3, 7)
    transicaoLateral(2, 10, 3, 9)
    transicaoLateral(3, 3, 4, 1)
    transicaoLateral(3, 8, 4, 3)
    transicaoLateral(3, 10, 4, 5)
    transicaoLateral(4, 2, 5, 4)
    transicaoLateral(4, 4, 5, 6)
    transicaoLateral(5, 1, 6, 1)
    transicaoLateral(5, 2, 6, 2)
    transicaoLateral(5, 3, 6, 3)
    transicaoLateral(5, 5, 6, 4)

    # seta posição da banana
    barras[6].getIndice(5).setFinal(True)

    # adiciona os custos reais dos nós
    adicionaCustoReal()

    # adiciona as heurísticas dos nós
    adicionaHeuristica()


def transicaoLateral(coluna1, indiceC1, coluna2, indiceC2):
    no1 = barras[coluna1].getIndice(indiceC1)
    no2 = barras[coluna2].getIndice(indiceC2)

    if no1 != None and no2 != None:
        no1.setTroca(no2)
        no2.setTroca(no1)


def adicionaCustoReal():
    for i in range(7):
        for j in range(barras[i].getTamanho()):
            barras[i].getIndice(j).setCustoReal((7-(i+1))+abs(6-(j+1)))
    barras[0].getIndice(6).setCustoReal(30)
    barras[1].getIndice(12).setCustoReal(30)
    barras[2].getIndice(13).setCustoReal(30)
    barras[3].getIndice(10).setCustoReal(30)
    barras[4].getIndice(5).setCustoReal(30)
    barras[5].getIndice(6).setCustoReal(30)


def adicionaHeuristica():
    for i in range(7):
        for j in range(barras[i].getTamanho()):
            if barras[i].getIndice(j).getTroca() != None:
                if getIndiceBarraVizinha(barras[i].getIndice(j).getTroca(), i) < i:
                    barras[i].getIndice(j).setHeuristica((7-(i+1))+1)
                else:
                    barras[i].getIndice(j).setHeuristica((7-(i+1))-1)
            else:
                barras[i].getIndice(j).setHeuristica(7-(i+1))

# retorna o indice da barra de um determinado nó


def getIndiceBarraVizinha(no, barraAtual):
    if barraAtual - 1 >= 0:
        noTmp = barras[barraAtual-1].getInicio()
        while noTmp != None:
            if noTmp == no:
                return barraAtual - 1
            noTmp = noTmp.getProximo()
    if barraAtual + 1 <= 6:
        noTmp = barras[barraAtual+1].getInicio()
        while noTmp != None:
            if noTmp == no:
                return barraAtual + 1
            noTmp = noTmp.getProximo()


if __name__ == "__main__":
    main()
