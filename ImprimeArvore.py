from NoArvore import NoArvore


def imprimeArvore(raizArvore: NoArvore, nomeBusca):

    f = open(f"arvores/{nomeBusca}.dot", "w")

    f.write("graph "+nomeBusca+" {\n")

    __auxImprimeArvore(f, raizArvore, raizArvore.getNoLista().getNome(), [])

    f.write("}")

    f.close()


def __auxImprimeArvore(f, no: NoArvore, nome: str, auxVet):
    if no != None:
        filhos = no.getFilhos()
        auxVet.append(nome)
        for i in range(len(filhos)):
            nomeFilho = filhos[i].getNoLista().getNome()
            while nomeFilho in auxVet:
                nomeFilho = nomeFilho + "*"
            f.write("\t\""+nome+"\" -- \"" +
                    nomeFilho+"\"\n")
            __auxImprimeArvore(f, filhos[i], nomeFilho, auxVet)
