#TRATAMENTO DE EXCEÇÕES

#Estrutura básica
try:
    numero = int(input("Número inteiro: "))
except ValueError:
    print("Favor inserir um número inteiro!")
else:
    print(numero)

#Solicitando o dado correto em loop
while True:
    try:
        numero = int(input("Número inteiro: "))
    except ValueError:
        print("Favor inserir um número inteiro!")
    else:
        print(numero)
        break

#Solicitando o dado correto em loop, de um número entre 10 e 20
while True:
    try:
        numero = int(input("Número inteiro: "))
        if not(numero >= 10 and numero <= 20):
            raise ValueError()
    except ValueError:
        print("Favor inserir um número inteiro entre 10 e 20!")
    else:
        print(numero)
        break

#Validando texto
while True:
    try:
        nome = input("Nome: ")
        if not(nome.isalpha()):
            raise ValueError()
    except ValueError:
        print("Favor inserir um nome válido!")
    else:
        print(nome)
        break


'''
EXERCÍCIO 11

Criar um aplicativo que realize o cadastro do estilo musical, contendo as seguintes informações:
Nome, idade, estilo musical e qtde de horas que passa ouvindo por dia.

A idade precisa estar entre 18 e 99 anos.
A quantidade de horas precisa ser entre 0 e 24 horas.

Após o cadastro, exportar os dados para o Excel.
'''
from pathlib import Path
import pandas as pd

#criar listas
lista_nome = []
lista_idade = []
lista_estilo = []
lista_horas = []

#Lista de tuplas
lista_tuplas_estilo_musical = []

resposta = "S"

while resposta.upper() == "S":
    while True:
        try:
            nome = input("Nome: ")
            if not(nome.isalpha()):
                raise ValueError()
        except ValueError:
            print("Favor inserir um nome válido!")
        else:
            lista_nome.append(nome)
            break

    while True:
        try:
            idade = int(input("Idade: "))
            if not(idade >= 18 and idade <= 99):
                raise ValueError()
        except ValueError:
            print("Favor inserir uma idade entre 18 e 99 anos!")
        else:
            lista_idade.append(idade)
            break
    
    while True:
        try:
            estilo = input("Estilo musical: ")
            if not(estilo.isalpha()):
                raise ValueError()
        except ValueError:
            print("Favor inserir um estilo válido!")
        else:
            lista_estilo.append(estilo)
            break   

    while True:
        try:
            horas = int(input("Horas ouvindo por dia: "))
            if not(horas >= 0 and horas <= 24):
                raise ValueError()
        except ValueError:
            print("Favor inserir uma quantidade entre 0 e 24 horas!")
        else:
            lista_horas.append(horas)
            break

    while True:
        try:
            resposta = input("Deseja inserir um novo registro? (S para sim e N para não)")
            if (resposta.upper() != "S" and resposta.upper() != "N"):
                raise ValueError()
        except ValueError:
            print("Favor informar S para sim ou N para não!")
        else:
            break
else:
    #criação da tupla
    for i in range(len(lista_nome)):
        dados_estilo_musical = (lista_nome[i],lista_idade[i],lista_estilo[i],lista_horas[i])
        lista_tuplas_estilo_musical.append(dados_estilo_musical)


#Exportar os dados cadastrados para o Excel
import Aula05 as a05 #Importando os objetos do script Aula05

arquivo_excel_estilo_musical = a05.endereco / "estilo_musical.xlsx"

if (a05.endereco.exists()):
    if not (arquivo_excel_estilo_musical.exists()):
        estilo_musical = pd.DataFrame(lista_tuplas_estilo_musical)

        estilo_musical = estilo_musical.rename(columns={0:"Nome",1:"Idade",2:"Estilo",3:"Horas"})

        try:
            estilo_musical.to_excel(arquivo_excel_estilo_musical,sheet_name="estilo",index=False)
            print("Arquivo criado com sucesso!")
        except ValueError:
            ValueError() #Mensagem de erro de SISTEMA

    else:
        try:
            a05.adiciona_dados_excel(arquivo_excel_estilo_musical,"estilo",lista_tuplas_estilo_musical)
            print("Arquivo atualizado com sucesso!")
        except ValueError:
            ValueError()
else:
    print("Endereço não existe! Favor verificar!")



    