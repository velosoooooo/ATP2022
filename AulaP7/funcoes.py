import csv
import os
import matplotlib.pyplot as plt


def LerDataset():
    fnome = "alunos.csv"
    f4=open(fnome,encoding='utf8')
    f4.readline()
    csv_reader=csv.reader(f4,delimiter=",")
    alunos = []
    for row in csv_reader:
        alunos.append(row)
    f4.close
    return alunos

tudo = LerDataset()

def dist_alunos_curso(lista):
    dist = {}
    for aluno in lista:
        curso = aluno[2]
        nome = aluno[1]
        if curso in dist.keys():
            dist[curso] += 1
        else:
            dist[curso] = 1
    return dist

# cria coluna com MÉDIA
def calcular_media(lista):
    # id, nome, curso, tp1, tp2, tp3, tp4, media, escalao
    for linha in lista:
        if len(linha)>=8:  # lista já tem coluna com a MÉDIA
            break
        media=round((int(linha[3])+int(linha[4])+int(linha[5])+int(linha[6]))/4,1)  # arredonda a MÉDIA a uma casa decimal
        linha.append(media)
    return lista

# cria coluna com ESCALÃO
def calcular_escalao(lista):
    #id, nome, curso, tp1, tp2, tp3, tp4, media, escalao
    for linha in lista:
        if float(linha[7])  >=16.5 and float(linha[7])<=20:   linha.append("A [17-20]")
        elif float(linha[7])>=12.5 and float(linha[7])<16.5:  linha.append("B [13-16]")
        elif float(linha[7])>= 8.5 and float(linha[7])<=12.5: linha.append("C [09-12]")
        elif float(linha[7])>= 4.5 and float(linha[7])<=8.5:  linha.append("D [05-08]")
        elif float(linha[7])>=   0 and float(linha[7])<=4.5:  linha.append("E [01-04]")
    return lista
        
def tamanho_linha_lista(lista):
    alunos = LerDataset()
    for aluno in alunos:
        return len(aluno)

def grava_lista_ficheiro(lista):
    cabeçalho=['id_aluno','nome','curso','tpc1','tpc2','tpc3','tpc4']
    if tamanho_linha_lista(lista)>=8:
        cabeçalho.append('media')
    if tamanho_linha_lista(lista)==9:
        cabeçalho.append('escalao')
    #ficheiro=input("Qual o nome do ficheiro a gravar?")
    ficheiro='alunos.csv'
    with open(ficheiro, 'w',encoding='utf-8') as f:
        writer=csv.writer(f, delimiter=',', lineterminator='\n')
        writer.writerow(cabeçalho)
        for linha in lista:
            writer.writerow(linha)
            
def tabela_alunos (lista):
    # id, nome, curso, tp1, tp2, tp3, tp4, media, escalao
    linha_aux = 1
    media=""
    escalao=""
    print_cabeçalho = True
    for linha in lista:
        if print_cabeçalho:
            os.system("cls")
            print("""
    ---------------------------------------------------------------------------------------------------------
    |                                           LISTAGEM DE ALUNOS                                          |
    ---------------------------------------------------------------------------------------------------------
    |    ID       Nome                           Curso         TPC1  TPC2  TPC3  TPC4    Média      Escalão |
    ---------------------------------------------------------------------------------------------------------""")
            print_cabeçalho = False
        if len(linha)>=8: 
            media=linha[7]
        if len(linha)==9: 
            escalao=linha[8]
        print (f"      {linha[0]:>5}    {linha[1]:30}    {linha[2]:10}   {linha[3]:>4}  {linha[4]:>4}  {linha[5]:>4}  {linha[6]:>4}    {media:>6}    {escalao:>10}")
        if linha_aux % 20 == 0:
            opcao = input("\n    [ Tecla (p) para PARAR.   Qualquer outra para continuar. ]")
            if opcao=="p" or opcao=="P":
                return
            print_cabeçalho = True
        linha_aux += 1

def tabelar_distribibuicao(dicionario, titulo):
    linha = 1
    print_cabeçalho = True
    for distribuicao, quantidade in dicionario.items():
        if print_cabeçalho:
            os.system("cls")
            print("    -----------------------------------------------------------------")
            print("    |               DISTRIBUIÇÃO de ALUNOS por " +str(titulo.ljust(20," "))+" |")
            print("    -----------------------------------------------------------------")
            print("    |        " + str(titulo.ljust(30," ")) + "    Número de Alunos     |")
            print("    -----------------------------------------------------------------")
            print_cabeçalho = False
        print (f"         {distribuicao:<40}      {str(quantidade):<4}    ")
        if linha % 20 == 0:
            opcao = input("\n    [ Tecla 'p' para PARAR.   Qualquer outra para continuar. ]")
            if opcao=="p":
                return
            print_cabeçalho = True
        linha = linha + 1
        
def dist_alunos_escalão(lista):
    dist = {}
    for aluno in lista:
        escalao = aluno[8]
        nome = aluno[1]
        if escalao in dist.keys():
            dist[escalao] += 1
        else:
            dist[escalao] = 1
    return dist

def graficos (distrib):
    plt.bar(distrib.keys(), distrib.values())
    plt.xticks([x for x in range (0, len(distrib.keys()))], distrib.keys(), rotation=75)
    plt.subplots_adjust(left=0.1, bottom=0.25, right=0.9, top=0.9, wspace=0, hspace=0)
    plt.show()