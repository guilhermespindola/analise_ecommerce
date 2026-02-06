import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar o arquivo enviado
df = pd.read_csv('ecommerce_estatistica.csv')

#1 - Histograma
plt.figure(figsize=(10, 6))
sns.histplot(df['Preço'], bins=20, kde=True, color='blue')
plt.title('Distribuição de Preços')
plt.xlabel('Preço')
plt.show()

#2 - Dispersão (Avaliações vs Vendas
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='N_Avaliações', y='Qtd_Vendidos_Cod')
plt.title('Número de Avaliações vs Quantidade Vendida')
plt.show()

#3 - Mapa de Correlação
plt.figure(figsize=(12, 8))
# Selecionando apenas colunas numéricas para o heatmap
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='RdYlGn', fmt=".2f")
plt.title('Mapa de Calor de Correlação')
plt.show()

#4 - Gráfico de Barra
plt.figure(figsize=(10, 6))
df['Gênero'].value_counts().plot(kind='bar', color='orange')
plt.title('Quantidade de Produtos por Gênero')
plt.xticks(rotation=45)
plt.show()

#5 - Grafico de Pizza
plt.figure(figsize=(8, 8))
df['Temporada'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title('Distribuição por Temporada')
plt.ylabel('')
plt.show()

#6 Gráfico de Densidade (Nota)
plt.figure(figsize=(10, 6))
sns.kdeplot(df['Nota'], fill=True, color="purple")
plt.title('Densidade das Notas dos Produtos')
plt.show()

#7 - Gráfico de Regressão
plt.figure(figsize=(10, 6))
sns.regplot(data=df, x='Preço_MinMax', y='Qtd_Vendidos_Cod', line_kws={"color": "red"})
plt.title('Regressão: Preço vs Vendas')
plt.show()
