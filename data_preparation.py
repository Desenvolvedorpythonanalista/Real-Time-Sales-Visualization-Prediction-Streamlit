import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer

def carregar_dados(arquivo_csv):
    df = pd.read_csv(arquivo_csv)
    df['data_venda'] = pd.to_datetime(df['data_venda'], errors='coerce')
    return df

def preparar_dados(df):
    df = df.dropna(subset=['valor_total_venda'])  # Remove linhas onde o valor total da venda é NaN

    # Identificar colunas categóricas e numéricas
    colunas_categoricas = ['setor', 'marca', 'modelo', 'localizacao', 'fornecedor']
    colunas_numericas = ['preço', 'quantidade_estoque', 'número_vendas', 'desconto']

    # Separar variáveis independentes e dependentes
    X = df[colunas_categoricas + colunas_numericas]
    y = df['valor_total_venda']

    # Imputação de dados faltantes para colunas numéricas
    imputer = SimpleImputer(strategy='mean')
    X[colunas_numericas] = imputer.fit_transform(X[colunas_numericas])
    
    # Codificação one-hot para variáveis categóricas
    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(drop='first', sparse_output=False), colunas_categoricas),
            ('num', 'passthrough', colunas_numericas)
        ]
    )

    X_processed = preprocessor.fit_transform(X)
    
    # Separar os dados em conjuntos de treino e teste (30% teste e 70% treino)
    X_train, X_test, y_train, y_test = train_test_split(X_processed, y, test_size=0.3, random_state=42)
    
    return X_train, X_test, y_train, y_test, preprocessor
