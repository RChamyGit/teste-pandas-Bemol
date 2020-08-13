# Linguagem de Programação:
#  Crie relatórios com gráficos e tabelas (dataset de saída) que mostrem quem mais vendeu em tal unidade,
#   venda por vendedor e produto mais vendido. 
#   Sinta-se a vontade para incluir mais análises com a base disponibilizada. 
#   Após o término, envie-nos o algoritmo criado para tal análise, assim também com as imagens em PNG, JPEG ou JPG. 

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("Desafio - Relatório - Dados - Questão 1.csv", sep=",")

data.head()

print(data)

# LENTO DEMAIS
# data.plot(kind='bar',x='usuario',y='num_compra',color='red')
# plt.show()

#specifics

#parece SQL!
dataf = pd.DataFrame(data)
# print (dataf)
# print(dataf[dataf.columns[6]])

#remove caracteres q nao sejam . ou numerais
dataf[dataf.columns[6:8]] = dataf[dataf.columns[6:8]].replace('[^.0-9]', '', regex=True).astype(float)
print(dataf.head(5))


dataVendedores = dataf.groupby("nome")["valor_compra"].sum().sort_values(ascending = False)



print(" AFTER GROUP BY ", dataf.head(5))



#reduzido p acelerar desempenho
plotdata = dataVendedores.head(100)
plotdata.plot(kind='bar',x='nome',y='valor_compra',color='red')
plt.title("melhores 100 vendedores")
plt.show()

#FIM TOP VENDEDORES



#Faturamento vendas lojas

dataFiliais = dataf.groupby("Filial")["valor_compra"].sum().sort_values(ascending = False)
plotdata = dataFiliais.head(100)
plotdata.plot(kind='bar',x='Filial',y='valor_compra',color='red')
plt.title("Valor de vendas / filiais")
plt.show()



#QTD VENDAS POR LOJA
dataFiliais = dataf.groupby("Filial")["valor_compra"].count().sort_values(ascending = False)
plotdata = dataFiliais.head(100)
plotdata.plot(kind='bar',x='Filial',y='valor_compra',color='red')
plt.title("Total vendas por filial")
plt.show()


#PRODUTO MAIS VENDIDO

# df = pd.DataFrame({
#     'name':['john','mary','peter','jeff','bill','lisa','jose'],
#     'age':[23,78,22,19,45,33,20],
#     'gender':['M','F','M','M','M','F','M'],
#     'state':['california','dc','california','dc','california','texas','texas'],
#     'num_children':[2,0,0,3,2,1,4],
#     'num_pets':[5,1,0,5,2,2,3]
# })

# # df.plot(kind='scatter',x='num_children',y='num_pets',color='red')
# # plt.show()

# df[['gender','age']].groupby('gender').median()
# df.groupby("gender").median()
# df.groupby("gender")["age"].median().plot(kind='bar',x='gender',y='age',color='red')
# plt.show()
# df.plot(kind='bar',x='gender',y='age',color='red')
# plt.show()