'''
EXERCÍCIO 7

Seu diretor comercial te solicitou a criação de alguma coisa, onde fosse possível calcular o bônus dos/as vendedores/as, de acordo com o
atingimento de metas (somente com 2 casas decimais), cuja a regra é:

Atingimento = (Valor vendido/meta) * 100

O Bônus é calculado da seguinte forma:

- Atingimento menor que 100: Não há bônus
- Atingimento maior ou igual a 100 e menor ou igual a 105: 2% sobre o valor vendido do/a vendedor/a
- Atingimento maior que 105: 3% sobre o valor vendido do/a vendedor/a

O salário final do/a vendedor/a deve observar a seguinte regra:

Salário final = Salário base + bônus

Ao final, deve apresentar uma mensagem com as seguintes informações:

Vendedores abaixo da meta:
Nomes:
Atingimento:
Salário final:

Vendedores que bateram a meta entre 100 e 105:
Nomes:
Atingimento:
Bônus:
Salário final:

Vendedores que bateram a meta acima de 105:
Nomes:
Atingimento:
Bônus:
Salário final:

Suponha que os dados de entrada no sistema são:
Meta de vendas: 10.000
Salário base dos/as vendedores/as: 2.000

Vendedor: João
Valor vendido: 8.000

Vendedora: Maria
Valor vendido: 10.800

Vendedor: Sócrates
Valor vendido: 12.150

Vendedora: Isis
Valor vendido: 12.280

Vendedora: Ohana
Valor vendido: 10.390

Vendedor: Platão
Valor vendido: 10.032

Vendedora: Afrodite
Valor vendido: 8.950
'''
#Criando listas
#listas abaixo da meta
lista_nome_abaixo_meta = []
lista_atingimento_abaixo_meta = []
lista_salario_final_abaixo_meta = []

#listas que atingiram a meta, entre 100 e 105
lista_nome_meta_100_105 = []
lista_atingimento_meta_100_105= []
lista_bonus_meta_100_105 =[]
lista_salario_final_meta_100_105 = []

#listas que atingiram a meta, acima 105
lista_nome_meta_105 = []
lista_atingimento_meta_105= []
lista_bonus_meta_105 =[]
lista_salario_final_meta_105 = []

#variáveis gerais
valor_meta = 10000
salario_base = 2000

#Capturando dados
nome = input("Nome:")
valor_vendido = int(input("Valor vendido(R$):"))

#Cálculo de atingimento da meta
atingimento = (valor_vendido/valor_meta)*100
atingimento = round(atingimento,2)

#Cálculo do valor de bônus
if (atingimento < 100): 
    #NÃO há bônus
    lista_nome_abaixo_meta.append(nome)
    lista_atingimento_abaixo_meta.append(atingimento)
    lista_salario_final_abaixo_meta.append(salario_base)
elif (atingimento >=100 and atingimento<=105):
    #Atingimento entre 100 e 105
    valor_bonus = (valor_vendido*2/100)
    salario_final = salario_base + valor_bonus

    lista_nome_meta_100_105.append(nome)
    lista_atingimento_meta_100_105.append(atingimento)
    lista_bonus_meta_100_105.append(valor_bonus)
    lista_salario_final_meta_100_105.append(salario_final)
elif (atingimento > 105):
    #Atingimento maior que 105
    valor_bonus = (valor_vendido*2/100)
    salario_final = salario_base + valor_bonus

    lista_nome_meta_105.append(nome)
    lista_atingimento_meta_105.append(atingimento)
    lista_bonus_meta_105.append(valor_bonus)
    lista_salario_final_meta_105.append(salario_final)
else:
    print("O atingimento calculado não satisfaz nenhuma das condições!")

#Exibindo os dados, separados por atingimento de meta.
print("")
print("Vendedores/as abaixo da meta:")
print("Nomes:",lista_nome_abaixo_meta)
print("Atingimento da meta %:",lista_atingimento_abaixo_meta)
print("Salário final(R$):", lista_salario_final_abaixo_meta)
print("")
print("Vendedores/as que atingiram a meta, entre 100 e 105:")
print("Nomes:",lista_nome_meta_100_105)
print("Atingimento da meta %:",lista_atingimento_meta_100_105)
print("Bônus (R$):",lista_bonus_meta_100_105)
print("Salário final(R$):", lista_salario_final_meta_100_105)
print("")
print("Vendedores/as que atingiram a meta, acima de 105:")
print("Nomes:",lista_nome_meta_105)
print("Atingimento da meta %:",lista_atingimento_meta_105)
print("Bônus (R$):",lista_bonus_meta_105)
print("Salário final(R$):", lista_salario_final_meta_105)

#ESTRUTURAS DE REPETIÇÃO
#for: Nos possibilita percorrer em todos os itens de um determinado conjunto de dados
#while: Noa possibilita percorrer em um conjunto de dados, de acordo com uma condição específica. 
#   Isso quer dizer que, enquanto a condição for Verdadeira, o loop seguirá executando suas ações

#Exemplo for
for i in lista_nome_meta_100_105:
    print(i)

for i in lista_nome_meta_105:
    print(i)

#Exemplo FOR com ELSE
for i in lista_nome_meta_105:
    print(i)
else:
    print("Todos/as os vendedores/as com atingimento acima de 105 foram exibidos!")

#Exemplo FOR com ELSE e FOR
print("Vendedores que atingiram a meta, acima de 105%:")
for i in lista_nome_meta_105:
    print(i)
else:
    print("")
    print("Vendedores com atingimento de meta, entre 100 e 105%:")
    for i in lista_nome_meta_100_105:
        print(i)

#Exemplo While
i = 0
while i < 5:
    print(i)
    #i=i+1
    i+=1

#Exemplo While com listas e perguntas dinânicas
#Imagine que seja necessário criar um formulário de entrevistas, que armazenará o nome e a idade
#de cada entrevistado/a. Ao final exibir os dados armazenados
#Criando listas
lista_nome_entrevistado = []
lista_idade_entrevistado = []

#Variável para condição do While
resposta = "S"

while resposta.upper() == "S":
    #Captura de dados
    entrevistado = input("Nome: ")
    idade = int(input("Idade: "))

    #Armazenamento nas listas
    lista_nome_entrevistado.append(entrevistado)
    lista_idade_entrevistado.append(idade)

    #Perguntar se há o desejo de inserir novos dados
    resposta = input("Deseja inserir novos dados?(S para sim. N para não): ")

print("Nomes:",lista_nome_entrevistado)
print("Idades:",lista_idade_entrevistado)

#Exemplo de While com Else e If
#Utilizando o cenário acima. Imagine que o usuário/a seja perguntado se ele deseja ou não
#exibir os dados das listas da tela (print)
#Criando listas
lista_nome_entrevistado = []
lista_idade_entrevistado = []

#Variável para condição do While
resposta = "S"

while resposta.upper() == "S":
    #Captura de dados
    entrevistado = input("Nome: ")
    idade = int(input("Idade: "))

    #Armazenamento nas listas
    lista_nome_entrevistado.append(entrevistado)
    lista_idade_entrevistado.append(idade)

    #Perguntar se há o desejo de inserir novos dados
    resposta = input("Deseja inserir novos dados?(S para sim. N para não): ")
else:
    impressao = input("Deseja exibir os dados? (S para sim. N para não)")
    if (impressao.upper() == "S"):
        print("Nomes:",lista_nome_entrevistado)
        print("Idades:",lista_idade_entrevistado)
    else:
        print("Finalizando o aplicativo. Obrigado! :)")

'''
EXERCÍCIO 8 (Baseado no Exercício 7)

O Diretor comercial percebeu que alguns vendedores superaram muito a meta e, por conta disso, 
resolveu acrescentar um bônus para todos/as que atingiram 120 ou mais.

O cálculo desse bônus será o seguinte:

A cada 1 ponto acima de 120, acrescentar R$ 150.
(atingimento de meta - 120)*150

Dessa forma, ele te solicitou esse ajuste e pediu para que no final fosse exibida uma mensagem com o nome, 
o bônus de excelência e o salário final, acrescido do bônus.

'''
#variáveis gerais
atigimento_excelencia = 120
valor_bonus_excelencia = 150

#Criado listas
lista_nome_excelencia = []
lista_bonus_excelencia = []
lista_salario_excelencia = []

for i in range(len(lista_nome_meta_105)):
    if (lista_atingimento_meta_105[i] >= atigimento_excelencia):
        #cálculo do bônus
        bonus_excelencia = (lista_atingimento_meta_105[i] - atigimento_excelencia)*150
        bonus_excelencia = round(bonus_excelencia,2)

        #Cálculo do bônus
        salario_excelencia = (lista_salario_final_meta_105[i] + bonus_excelencia)
        salario_excelencia = round(salario_excelencia,2)

        #adicionar as listas
        lista_nome_excelencia.append(lista_nome_meta_105[i])
        lista_bonus_excelencia.append(bonus_excelencia)
        lista_salario_excelencia.append(salario_excelencia)
else:
    impressao_excelencia = input("Bônus excelência calculado. Deseja visualiza os dados?(S para sim. N para não)")
    if (impressao_excelencia.upper() == "S"):
        i = 0
        print("")
        print("Vendedores de exclência:")
        print("*************************")
        while i < len(lista_nome_excelencia):
            print("- Nome: ",lista_nome_excelencia[i])
            print("- Bônus: ",lista_bonus_excelencia[i])
            print("- Salário Final: ", lista_salario_excelencia[i])
            print("")
            i = i + 1 #ou i+=1
    else:
        print("Aplicativo finalizado. Obrigado!")
