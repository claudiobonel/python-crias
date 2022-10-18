# Link para coleta de dados da web >> https://ibge.gov.br/explica/codigos-dos-municipios.php
# Coletando dados dos municípios do RJ, disponíveis no Link acima!

import pandas as pd
from Aula05 import endereco #Importa somente o objeto em questão

#Forma 1
#municipio = pd.read_html("https://ibge.gov.br/explica/codigos-dos-municipios.php")
#municipio = pd.DataFrame(municipio[19])
#municipio

#Forma 2
municipio = pd.read_html("https://ibge.gov.br/explica/codigos-dos-municipios.php",match="Municípios do Rio de Janeiro")
municipio = pd.DataFrame(municipio[0])
municipio = municipio.rename(columns={"Municípios do Rio de Janeiro":"municipios","Códigos":"mcirc"})
#municipio

#Colentando dados de um arquivo CSV
#Dados públicos extrados do ISP Dados RJ (Instituto de Segurança Pública do RJ)
arquivo_ocorrencias_csv = endereco / "ocorrencias.csv"

ocorrencia = pd.DataFrame(pd.read_csv(arquivo_ocorrencias_csv))
#ocorrencia

#Relacioando Dataframes (muncipio[mcirc] com ocorrencia[mcirc])
df_ocorrencia = pd.merge(ocorrencia,municipio,on=["mcirc"],how="inner")
#df_ocorrencia

#Filtrando DataFrame
#Ano
df_ocorrencia = df_ocorrencia.query("ano >= 2021")

#Ocorrencias
df_ocorrencia = df_ocorrencia.query("ocorrencias == 'roubo_veiculo' or ocorrencias == 'furto_veiculos'")
#df_ocorrencia

#Filtrando colunas
df_rank_muncipios = df_ocorrencia[["municipios","qtde"]]
df_rank_muncipios

#Consolidar a qtde através da soma, agrupando os municípios
df_rank_muncipios = df_rank_muncipios.groupby(["municipios"])["qtde"].sum()
df_rank_muncipios = pd.DataFrame(df_rank_muncipios)
df_rank_muncipios = df_rank_muncipios.reset_index()

#Ranquear os TOP 10 municípios pela quantidade total de roubos e furto de veículos, 
# a partir de 2021
df_rank_muncipios = df_rank_muncipios.nlargest(10,"qtde")

df_rank_muncipios