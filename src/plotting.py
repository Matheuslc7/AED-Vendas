import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Function of viewing the main customers by quantity Functions for Visualization
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
    plt.savefig("images/top_clientes_quantidade.png")
    plt.show()

#Function of viewing the main customers by value
def plot_top_clientes_valor(df):
    """Gera gráfico dos 10 clientes que mais compraram (Valor Total)."""
    top_clientes_valor = df.groupby("Cliente")["Vr. Total"].sum().sort_values(ascending=False).head(10)
    plt.figure(figsize=(12, 6))
    ax = sns.barplot(x=top_clientes_valor.index, y=top_clientes_valor.values, palette='Reds_r')
    plt.title("Top 10 Clientes que Mais Compraram - Valor Total", fontsize=14)
    plt.xlabel("Cliente")
    plt.ylabel("Valor Total (R$)")
    plt.xticks(rotation=45)
    for p in ax.patches:
        ax.annotate(f'R$ {p.get_height():,.2f}', (p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='bottom', fontsize=10, color='black')
    plt.savefig("images/top_clientes_valores.png")
    plt.show()

#Function of the main references by quantity solddef plot_top_ref_quantidade(df):
def plot_top_ref_quantidade(df):
    """Gera gráfico das referências mais vendidas (Quantidade)."""
    top_referencias_qtd = df.groupby("Referência")["Quantidade"].sum().sort_values(ascending=False).head(10)
    plt.figure(figsize=(12, 6))
    ax = sns.barplot(x=top_referencias_qtd.index, y=top_referencias_qtd.values, palette='Greens_r')
    plt.title("Top 10 Referências Mais Vendidas - Quantidade", fontsize=14)
    plt.xlabel("Referência")
    plt.ylabel("Quantidade")
    plt.xticks(rotation=45)
    plt.legend(["Quantidade"], loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=1)
    for p in ax.patches:
        ax.annotate(f'{p.get_height():,.0f}', (p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='bottom', fontsize=10, color='black')
    plt.savefig("images/top_referencias_quantidade.png")
    plt.show()

#Function of the main references by value
def plot_top_ref_valor(df):
    top_referencias_valor = df.groupby("Referência")["Vr. Total"].sum().sort_values(ascending=False).head(10)
    plt.figure(figsize=(12, 6))
    ax = sns.barplot(x=top_referencias_valor.index, y=top_referencias_valor.values, palette='Oranges_r')
    plt.title("Top 10 Referências Mais Vendidas - Valor Total", fontsize=14)
    plt.xlabel("Referência")
    plt.ylabel("Valor Total (R$)")
    plt.xticks(rotation=45)
    plt.legend(["Valor Total (R$)"], loc='upper center', bbox_to_anchor=(0.5, 1.15), ncol=1)
    for p in ax.patches:
        ax.annotate(f'R$ {p.get_height():,.2f}', (p.get_x() + p.get_width() / 2, p.get_height()), ha='center', va='bottom', fontsize=10, color='black')
    plt.savefig("images/top_referencias_valor.png")
    plt.show()

