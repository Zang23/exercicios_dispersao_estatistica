import numpy as np
import pandas as pd
from collections import Counter

df = pd.read_csv("dados_tratados_dolar.csv", sep=",")

compra = df["compra"]
data = df['datas']

#Frequencia absoluta

freqAbsoluta = Counter(compra)

#transformando em dataframe

tabela = pd.DataFrame.from_dict(freqAbsoluta, orient="index")

#colocar em ordem crescente
tabela = tabela.sort_index(ascending=True)

#colocar os indices reais
tabela.reset_index(inplace=True)

#Renomear colunas

tabela = tabela.rename(columns={"index": "valor"})

tabela = tabela.rename(columns={0: "freq_abs"})

#incluir frequencia relativa na tabela

tabela['freq_relativa'] = tabela['freq_abs'] / tabela['freq_abs'].sum()

#Frequencia percentual relativa

tabela['freq_rel_perc'] = tabela['freq_relativa']*100


#incluir frequencia acumulada

tabela['freq_acum'] = tabela['freq_abs'].cumsum()


#tabeka de ckasses de frequencia

print(tabela.valor.min())
print(tabela.valor.max())

#amplitude
dif = tabela['valor'].max() - tabela['valor'].min()


#criando classes

classes = [5.3,5.4,5.5,5.6,5.7]

labels = ["5.3 - 5.4 " , "5.4 - 5.5 " , "5,5 - 5.6 ", "5,6 - 5.7"]

intervalos = pd.cut(x = tabela.valor, bins = classes, labels=labels, include_lowest=True)

freq_abs = pd.value_counts(intervalos)



