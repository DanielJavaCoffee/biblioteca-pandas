import pandas as pd

# visualização de dados
import seaborn as sns
import matplotlib.pyplot as plt

# pip install plotly
# pip install cufflinks
# pip install chart-studio

import chart_studio.plotly as py
import cufflinks as cf

import  plotly.graph_objects as go
import plotly.express as px
import plotly.offline as pyo



varejo = pd.read_excel('C:/Users/danie/PycharmProjects/CaseNegocio/data/varejo.xlsx')

# Visualizando as categorias.
varejo["idcanalvenda"] = varejo["idcanalvenda"].str.replace("APP", "Aplicativo") # Trocando o APP por Aplicativo.
quantidade_de_compras = varejo.groupby("idcanalvenda").idcompra.nunique() # Fazendo a contagem por "categoria".
print(quantidade_de_compras)

quantidade_de_bandeiras = varejo.groupby("bandeira").idcompra.nunique()
print(quantidade_de_bandeiras)

varejo["Nome_Departamento"] = varejo["Nome_Departamento"].str.replace(" ","_")
quantidade_de_departamentos = varejo.groupby("Nome_Departamento").idcompra.nunique()
print(quantidade_de_departamentos)

varejo["estado"].fillna("MS", inplace = True)
quantidade_de_estados = varejo.groupby("estado").idcompra.nunique()
print(quantidade_de_estados)

# Ajustando os preços
media_de_preco = varejo["Preço"].mean()
varejo["Preço"].fillna(media_de_preco, inplace = True)

# Tratandos os dados nulos.
dados_nulos = varejo[varejo["estado"].isnull()]
dados_sem_nulos = varejo.dropna()

print(varejo[["Preço", "Preço_com_frete"]].describe())

"""
    Primeira regra. O Preço de Frete não pode ser maior que o Preço. 
"""

preco_errado = varejo.query("Preço > Preço_com_frete")
preco_certo = varejo.query("Preço < Preço_com_frete")

# Departamentos mais vendidos 01
departamentos_mais_vendidos = preco_certo.groupby("Nome_Departamento").idcompra.nunique().sort_values(ascending = False).reset_index()
print(departamentos_mais_vendidos)

# Média de preços por departamento
departamentos_media_precos = round(preco_certo.groupby("Nome_Departamento")["Preço_com_frete"].agg("mean").sort_values(ascending = False).reset_index(), 2)
print(departamentos_media_precos)

# Filtrar por datas ou meses específicos
departamentos_por_datas = preco_certo.groupby("Data").idcompra.nunique().sort_values(ascending = False).reset_index()
print(departamentos_por_datas)


# preco_certo.loc[:, "Mes"] = preco_certo["Data"].dt.month
# O uso de .loc garante que você está acessando e modificando o DataFrame original, e não uma cópia.
preco_certo["Mes"] = preco_certo["Data"].dt.month
departamentos_por_mes = preco_certo.groupby("Mes").idcompra.nunique().sort_values(ascending = False).reset_index()
print(departamentos_por_mes)

cliente_varejo = pd.read_excel('C:/Users/danie/PycharmProjects/CaseNegocio/data/cliente_varejo.xlsx')

print(cliente_varejo.head())

print(round(cliente_varejo[["idade", "renda"]].describe()))

cliente_varejo["renda"] = cliente_varejo["renda"].astype(float)

print(cliente_varejo.info())

vendas_clientes = preco_certo.merge(cliente_varejo, how = "left", on = "cliente_Log")
print(vendas_clientes.head())

agg_idcanal_renda = round(vendas_clientes.groupby("idcanalvenda")["renda"].agg("mean").sort_values(ascending = False).reset_index(), 2)
print(agg_idcanal_renda)

agg_idade_media_por_clientes = round(vendas_clientes.groupby("bandeira")["idade"].agg("mean").sort_values(ascending = False).reset_index(), 2)
print(agg_idade_media_por_clientes)

# Visualização de idade por bandeiras
plt.bar(agg_idade_media_por_clientes["bandeira"], agg_idade_media_por_clientes["idade"], color = "green")
plt.ylabel("Média de Idade")
plt.title("Idade média por bandeira", fontsize = 18, fontweight = "bold", color = "black")
plt.show()

# Visualização de renda por categoria
plt.bar(agg_idcanal_renda["idcanalvenda"], agg_idcanal_renda["renda"])
plt.ylabel("Média de Renda por Categoria")
plt.title("Média de vendas Por categoria", fontsize = 18, fontweight = "bold", color = "black")
plt.show()

# Gráfico de linha
vendas_data = preco_certo.groupby("Data").nunique().reset_index()
print(vendas_data)

plt.xlabel("Data de vendas")
plt.ylabel("Quantidade de vendas")
plt.title("Quantidade de compras por data", fontsize = 18, fontweight = "bold", color = "black")
x = vendas_data["Data"]
y = vendas_data["idcompra"]
plt.plot(x, y, color = "green", linewidth = 2)
plt.show()

fig = px.bar(agg_idade_media_por_clientes, x = "bandeira", y = "idade")
# Renderiza o gráfico offline
pyo.plot(fig, filename="grafico.html")