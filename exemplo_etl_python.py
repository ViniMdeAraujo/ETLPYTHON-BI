# -*- coding: utf-8 -*-
"""EXEMPLO_ETL - PYTHON

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10dF8OpDTzG7mUNerAgQE6Y8MTuwZoZiK
"""

import pandas as pd

vendas_filial1 = pd.read_csv('/content/vendas_filial1.csv')
vendas_filial2 = pd.read_excel('/content/vendas_filial2.xlsx')

print ("Dados da Filial1:")
print (vendas_filial1.head())
print ("\nDados da Filial 2:")
print (vendas_filial2.head())

import pandas as pd

vendas_filial1 = pd.read_csv('/content/vendas_filial1.csv')
vendas_filial2 = pd.read_excel('/content/vendas_filial2.xlsx')

vendas_filial1['Valor Total'] = vendas_filial1['Quantidade Vendida'] * vendas_filial1['Preco Unitario']
vendas_filial2['Valor Total'] = vendas_filial2['Quantidade Vendida'] * vendas_filial2['Preço Unitário']

print ("Dados Transformados da Filial1:")
print (vendas_filial1.head())
print ("\nDados Transformados da Filial 2:")
print (vendas_filial2.head())

import pandas as pd

vendas_filial1.to_csv ('vendas_filial1_transformadas.csv')
vendas_filial2.to_csv ('vendas_filial2_transformadas.csv')

dados_filial1 = pd.read_csv('vendas_filial1_transformadas.csv')
dados_filial2 = pd.read_csv('vendas_filial2_transformadas.csv')

print("Dados transformados da Filial1 (do arquivo CSV):")
print(dados_filial1.head())
print("\nDados transformados da Filial2 (do arquivo CSV):")
print(dados_filial2.head())

import sqlite3

conn = sqlite3.connect('dados_transformados.db')

vendas_filial1.to_sql ('vendas_filial1_transformadas', conn, index=False, if_exists='replace')
vendas_filial2.to_sql ('vendas_filial2_transformadas', conn, index=False, if_exists='replace')

dados_filial1 = pd.read_sql('SELECT * FROM vendas_filial1_transformadas', conn)
dados_filial2 = pd.read_sql('SELECT * FROM vendas_filial2_transformadas', conn)

print("Dados transformados da Filial1 (do banco de dados SQL):")
print(dados_filial1.head())
print("\nDados transformados da Filial2 (do banco de dados SQL):")
print(dados_filial2.head())

conn.close()

import sqlite3

conn = sqlite3.connect('dados_transformados.db')

cursor = conn.cursor()

cursor.execute('SELECT * FROM vendas_filial1_transformadas')

dados_filial1 = cursor.fetchall()

print ("Dados Transformados da Filial 1")
for linha in dados_filial1:
  print (linha)

cursor.execute ('SELECT * FROM vendas_filial2_transformadas')

dados_filial2 = cursor.fetchall()

print ("Dados Transformados da Filial 2")
for linha in dados_filial2:
  print (linha)

cursor.close()
conn.close()