from Aula07 import df_rank_muncipios
import numpy as np
import matplotlib.pyplot as plt


#Métricas da estatística descritiva, utilizando o numpy
totalQtde = np.sum(df_rank_muncipios["qtde"])
mediaQtde = np.average(df_rank_muncipios["qtde"])
medianaQtde = np.median(df_rank_muncipios["qtde"])
quantileQtde25 = np.quantile(df_rank_muncipios["qtde"],q=0.25)
quantileQtde50 = np.quantile(df_rank_muncipios["qtde"],q=0.50)
quantileQtde75 = np.quantile(df_rank_muncipios["qtde"],q=0.75)

print("Soma:", totalQtde)
print("Média:", mediaQtde)
print("Mediana:",medianaQtde)
print("Quantile 25%:",quantileQtde25)
print("Quantile 50%:",quantileQtde50)
print("Quantile 75%:",quantileQtde75)

#Cálculo de indicador
df_rank_muncipios["influencia"] = round((df_rank_muncipios["qtde"]/totalQtde),4)

df_rank_muncipios

#Visualização do dado, uilizando o matplotlib

#tamanho da área do gráfico
plt.figure(figsize=(13,3))

#Reordenar o dataframe
df_rank_muncipios = df_rank_muncipios.sort_values(by="influencia",ascending=True)

#plotar o gráfico
rk_municipios = plt.barh("municipios","influencia",data=df_rank_muncipios)

#título do gráfico
plt.title("Ranking de municípios")

#rótulo de dados
plt.bar_label(rk_municipios, padding=10)

#remover borda
plt.box(False)

#Removendo o eixo X
ex = plt.gca()
ex.get_xaxis().set_visible(False)

#Finalizando e exibindo o gráfico
plt.show(rk_municipios)