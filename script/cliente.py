import pandas as pd

cliente_varejo = pd.read_excel('C:/Users/danie/PycharmProjects/CaseNegocio/data/cliente_varejo.xlsx')

print(cliente_varejo.head())

print(round(cliente_varejo[["idade", "renda"]].describe()))

cliente_varejo["renda"] = cliente_varejo["renda"].astype(float)

print(cliente_varejo.info())