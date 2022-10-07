#Exportação de dados para o Excel

#Primeiro passo - Criação da tupla
lista_nomes = ["Claudio","Bonel","Silva","Maria","Joana","João","Maria","Carlos","José"]
lista_alturas = [1.90,1.81,1.96,1.75,1.70, 1.78,1.65,1.68,1.98]

lista_tupla_alturas = []

for i in range(len(lista_nomes)):
    dados_tupla = (lista_nomes[i],lista_alturas[i])
    lista_tupla_alturas.append(dados_tupla)

print(lista_tupla_alturas)

#Segundo passo - Exportação para o arquivo em Excel
#Bibilioteca é um conjunto de métodos com finalidades específicas

#Biblioteca para manipular arquivos no windows - Pathlib
from pathlib import Path

#Biblioteca para manipular dados em geral
import pandas as pd

#Definindo o endereço para exportação do arquivo
endereco = Path("C:\\Users\\claud\\OneDrive\\Claudio Bonel-DADOTECA\\Projetos Sociais\\Projeto Dado Humanizado\\Python Crias\\Dados")

#Definindo o nome do arquivo a ser exportado
arquivo_excel = endereco / "alturas.xlsx"

#Definindo uma função customizada de exportação para o Excel
def adiciona_dados_excel (arquivo, nome_planilha, dados):

    #Coletar os dados JÁ carregado
    df_origem = pd.read_excel(arquivo,sheet_name=nome_planilha)
    
    #Transformar df_origem em tupla
    tupla_origem = [tuple(x) for x in df_origem.values]

    #Verificar se os dados novos já existe no arquivo.
    #Se existir, não exporta. Do contrário adiciona ao arquivo.
    i = 0
    lista_dados_atualizados = []

    while i < len(dados):
        if (dados[i] not in tupla_origem): #Verifica se o dado novo NÃO existe no arquivo já carregado
            #Se NÃO existe! É um dado NOVO! Adicionar a lista de dados que SERÃO ATUALIZADOS no arquivo.
            lista_dados_atualizados.append(dados[i]) 
            i = i + 1
        else:
            i = i + 1

    #Transformar a tupla de dados a serem atualizados em um DATAFRAME
    df_dados_atualizados = pd.DataFrame(lista_dados_atualizados)

    #mode = a -> append
    with pd.ExcelWriter(arquivo,mode="a",engine="openpyxl",if_sheet_exists="overlay") as atualizar:
        df_dados_atualizados.to_excel(atualizar, sheet_name=nome_planilha,header=None,startrow=atualizar.sheets[nome_planilha].max_row,index=False)
    
#FIM DA FUNÇÃO de exportação para o Excel


#Estrutura de exportação para o Excel
if (endereco.exists()):
    #Variável nome das colunas
    colunas = {0:"Nome",1:"Altura"}

    if not (arquivo_excel.exists()): #Verifica se o arquivo NÃO existe, para exporta-lo pela primeira vez.
        #Criar um dataframe com a lista tupla alturas
        df_alturas = pd.DataFrame(lista_tupla_alturas)

        #Renomeando colunas - utilizando a variável de dicionário, representada por {}
        df_alturas = df_alturas.rename(columns = colunas)

        #Exportar para o Excel
        df_alturas.to_excel(arquivo_excel,sheet_name="alturas",index=False)

        print("Arquivo criado!")
    else: #Arquivo EXISTE e deverá ser atualizado.
        print("Arquivo sendo atualizado...")
        adiciona_dados_excel(arquivo_excel,"alturas",lista_tupla_alturas) #invoca a função criada por vc
        print("Arquivo atualizado! Obrigado!")
else:
    print("Endereço NÃO existe! Favor verificar!")



'''
def calculo_atingimento(valor,meta):
    atingimento = (valor/meta)*100
    print(atingimento)

calculo_atingimento(1000,1200)
'''