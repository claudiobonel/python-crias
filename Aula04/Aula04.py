'''
EXERCÍCIO 9

Um colecionador de discos de vinil, com mais de 5000 títulos, te pediu para você criar um programa, onde seja possível cadastrar o nome do/a artista, 
nome do disco e o ano de lançamento, de modo dinâmico, sempre perguntando se deseja cadastrar (ou não) um novo artista.

Ao final desse cadastro, ele gostaria de colocar para leilão beneficente alguns discos, considerando o seguinte:
- Se o ano for maior ou igual que 1960 e menor 1970, o valor será calculado da seguinte forma:
(ano atual - ano de lançamento do disco)*150

- Se o ano for maior ou igual a 1970 e menor que 1980, o valor será calculado da seguinte forma:
(ano atual - ano de lançamento do disco)*100

- Demais anos não serão colocados em leilão.

O programa de cadastro não deve enviar para leilão no momento da inserção, visto que o leilão beneficente só acontecerá uma vez e os discos 
continuarão sendo inseridos mesmo após o leilão! Portanto, a verificação dos discos que irão para leilão deve ser realizada uma única vez!

Suponha que os discos que serão cadastrados são:

Artista: Chuck Berry
Disco: Chuck Berry Is on Top
Ano: 1960

Artista: Sex Pistols
Disco: God Save The Queen
Ano: 1977

Artista: Ferris Wheel
Disco: Supernatural Girl
Ano: 1974

Artista: Pink Floyd
Disco: Ummagumma
Ano: 1969

Artista: Gorilla Biscuits
Disco: Gorilla Biscuits
Ano: 1987

Artista: Tim Maia
Disco: Racional
Ano: 1975

Artista: Raul Seixas
Disco: Let Me Sing My Rock'n'Roll
Ano: 1985

Artista: Dire Straits
Disco: Brothers in arms
Ano: 1985

Artista: The Clash
Disco: London Calling
Ano: 1979

Com relação ao leilão, ele pediu para que você registre o resultado separando os dados dos discos de 1960 a 1970, dos de 1970 a 1980. 
Por fim, o aplicativo deve possibilitar a impressão (ou não) dos registros. Caso o usuário opte por exibir os registros, possiblitar 
que o mesmo escolha o período de sua preferência, exibindo o artista, o nome do disco, o ano e o valor que o disco irá para o leilão.

'''
#CADASTRO DOS DISCOS
#Criar as listas
lista_artista = []
lista_disco = []
lista_ano = []

#Variável de resposta
resposta = 'S'

while resposta.upper() == 'S':
    #Solicitando dados
    artista = input("Artista: ")
    nome_disco = input("Nome do disco: ")
    ano_lancamento = int(input("Ano de lançamento: "))

    #Inserir os dados nas listas
    lista_artista.append(artista)
    lista_disco.append(nome_disco)
    lista_ano.append(ano_lancamento)

    #Perguntar se deseja realizar um novo cadastro
    resposta = input("Deseja inserir um novo artista? (S para sim. N para não)")
else:
    impressao = input("Deseja exibir os discos cadastrados? (S para sim. N para não)")
    if (impressao.upper() == 'S'):
        print("Artistas: ", lista_artista)
        print("Discos: ",lista_disco)
        print("Ano de lançamento: ", lista_ano)
    else:
        print("Cadastro finalizado!")

#CADASTRO DE DISCOS FINALIZADO

#INICIANDO A VERIFICAÇÃO DO LEILÃO
#Criando listas
lista_artista_1960_1970 = []
lista_disco_1960_1970 = []
lista_ano_1960_1970 = []
lista_valor_1960_1970 = []

lista_artista_1970_1980 = []
lista_disco_1970_1980  = []
lista_ano_1970_1980 = []
lista_valor_1970_1980 = []

#variavel de valor para leilão
aplicacao_valor_1960_1970 = 150
aplicacao_valor_1970_1980 = 100

#Verificação do ano de lançamento, para inserir nas listas do Leilão
for i in range(len(lista_ano)):
    if (lista_ano[i] >= 1960 and lista_ano[i] < 1970):
        #Calcular o valor para o leilão
        valor_1960_1970 = (2022 - lista_ano[i]) * aplicacao_valor_1960_1970

        #inserido dados nas listas
        lista_artista_1960_1970.append(lista_artista[i])
        lista_disco_1960_1970.append(lista_disco[i])
        lista_ano_1960_1970.append(lista_ano[i])
        lista_valor_1960_1970.append(valor_1960_1970)

    elif (lista_ano[i] >= 1970 and lista_ano[i] < 1980):
        #Calcular o valor para o leilão
        valor_1970_1980 = (2022 - lista_ano[i]) * aplicacao_valor_1970_1980

        #inserido dados nas listas
        lista_artista_1970_1980.append(lista_artista[i])
        lista_disco_1970_1980.append(lista_disco[i])
        lista_ano_1970_1980.append(lista_ano[i])
        lista_valor_1970_1980.append(valor_1970_1980)
else:
    impressao_leilao = input("Deseja exibir os discos para Leilão? (S para sim. N para não)")
    if (impressao_leilao.upper() == "S"):
        periodo_discos = int(input("Qual período que deseja exibir? (1 para 1960 até 1970. 2 para 1970 até 1980)"))

        #Variável para impressão dos dados do leilão.
        iDiscos = 0

        #Verifica o período escolhido para exibição
        if (periodo_discos == 1):
            print("Exibindo discos de 1960 a 1970:")
            print("********************************")
            while iDiscos < len(lista_artista_1960_1970):
                print("Artista: ", lista_artista_1960_1970[iDiscos])
                print("Disco: ", lista_disco_1960_1970[iDiscos])
                print("Ano: ",lista_ano_1960_1970[iDiscos])
                print("Valor leilão (R$): ", lista_valor_1960_1970[iDiscos])
                print("")
                iDiscos = iDiscos + 1
        else:
            print("Exibindo discos de 1970 a 1980:")
            print("********************************")
            while iDiscos < len(lista_artista_1970_1980):
                print("Artista: ", lista_artista_1970_1980[iDiscos])
                print("Disco: ", lista_disco_1970_1980[iDiscos])
                print("Ano: ",lista_ano_1970_1980[iDiscos])
                print("Valor leilão (R$): ", lista_valor_1970_1980[iDiscos])
                print("")
                iDiscos = iDiscos + 1       
    else:
        print("Aplicação finalizada. Obrigado!")     

#FINALIZAÇÃO DA VERIFICAÇÃO DE DISCOS PARA O LEILÃO

#TUPLA
#As tuplas são VARIÁVEIS e são utilizadas quando há a necessidade de criar junções entre dados (que fazem sentido) e
#além disso, podem (e vão) correlacionar listas de dados, ou seja, podemos unir todas as listas em tuplas, realizando a junção
#através de seus índices
#
#As listas são representadas por []. Já as tuplas são representadas por ()

#EXEMPLO
#Imagine que nós já realizamos um cadastro de nomes e alturas e os dados foram armazedos nas seguintes listas

lista_nomes = ["Bonel","Claudio","Silva"]
lista_altura = [1.80,1.90,1.75]

#Imgine que eu deseje apresentar os dados das listas, ordenando-os da maior para a menor altura

#Listas só podem ser ordenandas INDIVIDUALMENTE
#Se eu ordenar somente a lista_altura, teremos o seguinte:
#lista_altura.sort(reverse=True)
#print(lista_altura)
#print(lista_nomes)

#Criando um tupla para identificar a ordenação das alturas.

#criando lista de tuplas

lista_tupla_alturas = []

for i in range(len(lista_nomes)):
    dados_tupla = (lista_nomes[i],lista_altura[i])
    lista_tupla_alturas.append(dados_tupla)
else:
    print("Tuplas criadas e armazenadas na lista de alturas!")

print(lista_tupla_alturas)

#Ordenando a tupla
#lista_tupla_alturas.sort(key=1,reverse=True) #NÃO é possível informar nr inteiro, no argumento Key
#print(lista_tupla_alturas)

lista_tupla_alturas.sort(key=lambda x: x[1],reverse=True)
print("Nomes ordenados pela altura: ", lista_tupla_alturas)
print("Maior altura: ", lista_tupla_alturas[0])

#Variável para identificar a menor altura
ultimo_ind = len(lista_tupla_alturas)-1
print("Menor altura: ", lista_tupla_alturas[ultimo_ind])


'''
EXERCÍCIO 10

Após termos separado os discos para o leilão (Exercício 9), o colecionador te pediu para ajustar o aplicativo de modo a
possibilitar ao usuário a escolha do período (1960 a 1970 ou 1970 a 1980), para ser ordenando (ranqueado) pelo valor de leilão,
bem como se deseja exibir o resultado ou não.

'''
#criar lista da tupla
lista_tupla_discos = []

#criar variavel de ranqueamento
iRank = 0

#Perguntar qual período ordenar
rank_discos = int(input("Qual período deseja verificar o ranqueamento? (1 para 1960 a 1970. 2 para 1970 a 1980)"))

if (rank_discos == 1):
    for i in range(len(lista_artista_1960_1970)):
        #cria a tupla
        tupla = (lista_artista_1960_1970[i],lista_disco_1960_1970[i],lista_ano_1960_1970[i],lista_valor_1960_1970[i])

        #adiciona a tupla a lista
        lista_tupla_discos.append(tupla)
    else:
        impressao_rank = input("Deseja exibir o rank dos discos de 1960 a 1970? (S para sim. N para não)")
        if(impressao_rank.upper() == "S"):
            #Ordenar/Ranquear os dados da tupla, através do valor
            lista_tupla_discos.sort(key=lambda x: x[3], reverse=True)

            #exibir na tela
            print("Rank dos discos de 1960 a 1970:")
            print("*******************************")
            while iRank < len(lista_tupla_discos):
                print((iRank + 1),'º Lugar: ', lista_tupla_discos[iRank])
                iRank = iRank+1
        else:
            print("Aplicativo finalizado. Obrigado!")
else:
    for i in range(len(lista_artista_1970_1980)):
        #cria a tupla
        tupla = (lista_artista_1970_1980[i],lista_disco_1970_1980[i],lista_ano_1970_1980[i],lista_valor_1970_1980[i])

        #adiciona a tupla a lista
        lista_tupla_discos.append(tupla)
    else:
        impressao_rank = input("Deseja exibir o rank dos discos de 1970 a 1980? (S para sim. N para não)")
        if(impressao_rank.upper() == "S"):
            #Ordenar/Ranquear os dados da tupla, através do valor
            lista_tupla_discos.sort(key=lambda x: x[3], reverse=True)

            #exibir na tela
            print("Rank dos discos de 1960 a 1970:")
            print("*******************************")
            while iRank < len(lista_tupla_discos):
                print((iRank + 1),'º Lugar: ', lista_tupla_discos[iRank])
                iRank = iRank+1
        else:
            print("Aplicativo finalizado. Obrigado!")
    

