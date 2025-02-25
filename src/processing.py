import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path="data_input/vendas.xlsx"):
    """Carrega o arquivo Excel de vendas."""
    if os.path.exists(file_path):
        return pd.read_excel(file_path)
    else:
        print("Arquivo de dados não encontrado. Certifique-se de colocar 'vendas.xlsx' em 'data_input/'.")
        return None

# Carregar os dados
df = load_data()
df.head()  # Exibir as primeiras linhas para conferir

def plot_top_clientes_quantidade(df):
    """Gera gráfico dos 10 clientes que mais compraram (Quantidade)."""
    top_clientes_qtd = df.groupby("Cliente")["Quantidade"].sum().sort_values(ascending=False).head(10)
    plt.figure(figsize=(12, 6))
    ax = sns.barplot(x=top_clientes_qtd.index, y=top_clientes_qtd.values, palette='Blues_r')
    plt.title("Top 10 Clientes que Mais Compraram - Quantidade", fontsize=14)
    plt.xlabel("Cliente")
    plt.ylabel("Quantidade")
    plt.xticks(rotation=45)
    for p in ax.patches:
        ax.annotate(f'{p.get_height():,.0f}', (p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='bottom', fontsize=10, color='black')
    plt.show()
