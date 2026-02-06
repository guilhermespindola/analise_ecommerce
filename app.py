import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

df = pd.read_csv('ecommerce_estatistica.csv')
app = dash.Dash(__name__)

# CRIAÇÃO DOS GRÁFICOS

# Gráfico 1: Histograma de Preços
fig_hist = px.histogram(df, x="Preço", nbins=30, title="Distribuição de Preços", color_discrete_sequence=['#636EFA'])

# Gráfico 2: Dispersão (Preço vs Vendas)
fig_scatter = px.scatter(df, x="Preço", y="Qtd_Vendidos_Cod", color="Gênero", title="Preço vs Quantidade Vendida")

# Gráfico 3: Mapa de Calor (Correlação)
df_corr = df[['Nota_MinMax', 'N_Avaliações_MinMax', 'Desconto_MinMax', 'Preço_MinMax', 'Qtd_Vendidos_Cod']].corr()
fig_heatmap = px.imshow(df_corr, text_auto=True, title="Mapa de Calor de Correlação", color_continuous_scale='RdBu_r')

# Gráfico 4: Barras (Produtos por Gênero)
fig_bar = px.bar(df['Gênero'].value_counts().reset_index(), x='Gênero', y='count', title="Produtos por Gênero", color='Gênero')

# Gráfico 5: Pizza (Vendas por Temporada)
fig_pie = px.pie(df, values='Qtd_Vendidos_Cod', names='Temporada', title='Proporção de Vendas por Temporada')

app.layout = html.Div(style={'fontFamily': 'Arial, sans-serif', 'padding': '20px'}, children=[
    html.H1(children='Dashboard de E-commerce', style={'textAlign': 'center', 'color': '#2C3E50'}),
    html.P(children='Análise estatística e preditiva dos produtos.', style={'textAlign': 'center'}),

    html.Div([
        dcc.Graph(figure=fig_hist),
        dcc.Graph(figure=fig_scatter)
    ], style={'display': 'flex'}),

    html.Div([
        dcc.Graph(figure=fig_bar),
        dcc.Graph(figure=fig_pie)
    ], style={'display': 'flex'}),

    html.Div([
        dcc.Graph(figure=fig_heatmap)
    ])
])

if __name__ == '__main__':
    app.run(debug=True)