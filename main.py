
from googlesearch import search

from datetime import datetime




def URL(query):  # Responsável por fazer a consulta no google com base no termo do arquivo de entrada.

    return search(query, tld='com', lang='en', stop=100, pause=2)


def ler(nomeArq):  # Responsável por ler um dado arquivo.

    meuArquivo = open(nomeArq)

    conteudo = meuArquivo.readlines()

    meuArquivo.close()

    return conteudo


def escrever(nomeArquivo, argumento, urlEncontrada):  # Responsável pela escrita do arquivo
    arquivo = open(nomeArquivo, "a")
    linha = argumento.replace("\n", "") + "|" + urlEncontrada + "\n"
    arquivo.write(linha)
    arquivo.close()


def saida1(nomeArq):  # Responsável pelo tratamento ao arquivo de saída1

    for dadoEntrada in ler("entrada.txt"):

        for j in URL(dadoEntrada):
            escrever(nomeArq, dadoEntrada, j)





def saida2(): # Responsável pelo tratamento ao arquivo de saída2



        saida1("temporario.txt") #Faz uma segunda pesquisa.

        conjA = set(ler("saida.txt")) #criando o conjunto a

        conjB = set(ler("temporario.txt")) #criando o conjunto b

        diff = conjB.difference(conjA)

        for i in diff:

            #criando o arquivo de saída2

                dataHora = datetime.now().strftime('%d-%m-%Y %H:%M')

                escrever(f'saida2 {dataHora}.txt',i.split("|")[0], i.split("|")[1])









if __name__ == '__main__':

    #saida1("saida.txt")

    saida2()
