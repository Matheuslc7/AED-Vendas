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
