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

dataf = pd.DataFrame(data)
# print (dataf)
# print(dataf[dataf.columns[6]])

#remove caracteres q nao sejam . ou numerais
dataf[dataf.columns[6:8]] = dataf[dataf.columns[6:8]].replace('[^.0-9]', '', regex=True).astype(float)
print(dataf.head(5))


dataVendedores = dataf.groupby("nome")["valor_compra"].sum().sort_values(ascending = False)



print(" AFTER GROUP BY ", dataf.head(5))



#reduzido p acelerar desempenho

#vendedores c mais vendas
plotdata = dataVendedores.head(100)
plotdata.plot(kind='bar',x='nome',y='valor_compra',color='red')
plt.title("melhores 100 vendedores")
plt.show()




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



def questao2():
    data = pd.read_csv("Desafio - Relatório - Dados - Questão 2.csv", sep=",")
    print(data.groupby("produto")["quantidade"].sum().sort_values(ascending = False))
    dataf = pd.DataFrame(data)
    plotdata = dataf.groupby("produto")["quantidade"].sum().sort_values(ascending = False)
    print (plotdata.head(5))
    plotdata.plot(kind='bar',x='produto',y='quantidade',color='red')
    plt.title("Qtd vendas produto")
    plt.show()


def main():
    questao2()

if __name__ == "__main__":
    main()


#13-08-2020 first commit
#TODO separar datetime, suplots
