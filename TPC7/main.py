import funcoes as f

def main():
    print ("""
    -------------------------------------
    |          Menu Principal           |
    -------------------------------------
    (1) Menu
    (2) Ler DataSet
    (3) Apresentar Lista de alunos
    (4) Distribuição alunos por curso
    (5) Ver e adicionar (no ficheiro) as médias dos alunos
    (6) Distribuição alunos por escalão
    (7) Ver e adicionar (no ficheiro) os escalões dos alunos
    (8) Apresentar gráfico das distribuições
    (9) Apresenta 
    (0) Sair
    -------------------------------------
    """)

opcao = 2
while opcao != 0:
    main()
    opcao = int(input("Introduza a opção que deseja --> "))
    if opcao == 1:
        main()
    if opcao == 2:
        f.LerDataset()
    if opcao == 3:
        alunos=f.LerDataset()
        f.tabela_alunos(alunos)
    if opcao == 4:
        dist = f.dist_alunos_curso(f.LerDataset())
        print(dist)
        f.tabelar_distribibuicao(f.dist_alunos_curso(alunos),"CURSO")
        a = input("Pressione qualquer tecla e dê ENTER para voltar ao menu ")
    if opcao == 5:
        alunos = f.calcular_media(alunos)
        f.tabela_alunos(alunos)
    if opcao == 6:
        if f.tamanho_linha_lista(alunos)<8:
            print(f.tamanho_linha_lista(alunos))
            print("Tem que adicionar a coluna escalão")
        else:
            print(alunos)
            dista = f.dist_alunos_escalão(alunos)
            f.tabelar_distribibuicao(dista, "ESCALÃO")
    if opcao == 7:
        alunos=f.calcular_escalao(alunos)   
        f.tabela_alunos(alunos)
    if opcao == 8:
        distrib= input("\n      Que distribuição quer ver representada? (c)urso, (e)scalão:,")
        if distrib== "c" or distrib=="C":
            print (" \n            Distribuição por CURSO   ")
            f.graficos(f.dist_alunos_curso(alunos))
        elif distrib== "e" or distrib=="E":
            if f.tamanho_linha_lista(alunos)<7:
                print("\n      [ ERRO: Antes de pedir GRÁFICO é necessário Criar a DISTRIBUIÇÃO POR ESCALÃO. ]")
            else:
                print (" \n            Distribuição por ESCALÃO   ")
                f.graficos(f.dist_alunos_escalão(alunos))