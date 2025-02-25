# Análise de Vendas

Este repositório contém um projeto de análise de dados de vendas, onde são realizadas análises exploratórias e gerados gráficos para avaliar o desempenho dos clientes e produtos. O código analisa os dados contidos em um arquivo Excel chamado `vendas.xlsx`, realizando as seguintes tarefas:

- Estatísticas descritivas sobre as vendas.
- Identificação dos clientes que mais compraram, tanto em termos de quantidade quanto de valor total.
- Análise das referências mais vendidas, com foco em quantidade e valor total.

## Funcionalidades

1. **Análise Estatística Descritiva:**
   - Resumo das principais estatísticas sobre os dados (média, desvio padrão, valores mínimo e máximo, etc.).
   - Identificação de valores ausentes.
   
2. **Análise de Clientes:**
   - Geração de gráficos sobre os 10 clientes que mais compraram, tanto em termos de quantidade quanto de valor total.

3. **Análise de Referências:**
   - Geração de gráficos sobre as 10 referências mais vendidas, tanto em termos de quantidade quanto de valor total.

## Pré-requisitos

Para rodar este projeto, você precisará ter o Python instalado, junto com as bibliotecas necessárias. Aqui estão os passos para configurar o ambiente de desenvolvimento:

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/analise-vendas.git
cd analise-vendas
```

### 2. Criar um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
source venv/bin/activate  # No Linux/MacOS
venv\Scripts\activate     # No Windows
```

### 3. Instalar as dependências

Instale as bibliotecas necessárias usando o `pip`:

```bash
pip install -r requirements.txt
```

Ou, se preferir instalar manualmente:

```bash
pip install pandas matplotlib seaborn openpyxl
```

### 4. Estrutura de Arquivos

O projeto espera que você coloque o arquivo de dados `vendas.xlsx` dentro da pasta `data_input/`. Certifique-se de que o arquivo de vendas esteja presente no local correto para que o código funcione.

```plaintext
analise-vendas/
 ├── data_input/
 │   └── vendas.xlsx
 ├── images/
 │   └── [gráficos gerados]
 ├── src/
 |   └── aed_vendas.ipynb
 │   └── processing.py
 |   └── plotting.ipynb
└── main.py
└── requirements.txt
└── README.md
```

## Como Executar

1. Coloque o arquivo `vendas.xlsx` com os dados de vendas dentro da pasta `data_input/`.
2. Execute o script Python para realizar a análise e gerar os gráficos:

```bash
python main.py
```

Os gráficos gerados serão salvos na pasta `images/` como arquivos PNG, com os seguintes nomes:

- `top_clientes_quantidade.png`
- `top_clientes_valor.png`
- `top_referencias_quantidade.png`
- `top_referencias_valor.png`

## Resultados Esperados

Após a execução do código, você verá os seguintes resultados:

- **Gráficos de Análise dos Clientes:**
  - Top 10 clientes que mais compraram (quantidade e valor total).
  
- **Gráficos de Análise das Referências:**
  - Top 10 referências mais vendidas (quantidade e valor total).
  
Esses gráficos serão salvos na pasta `images/` para visualização.

## Contribuindo

1. Faça um fork deste repositório.
2. Crie uma branch para sua feature (`git checkout -b minha-feature`).
3. Faça as alterações necessárias.
4. Envie um pull request para este repositório.

## Contato

Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para abrir uma *issue* ou entrar em contato.
