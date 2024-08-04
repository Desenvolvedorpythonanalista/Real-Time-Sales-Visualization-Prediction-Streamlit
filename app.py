import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
from data_preparation import carregar_dados, preparar_dados
from model_training import treinar_modelo, avaliar_modelo
import sys
import os

# Adiciona o diretório atual ao caminho de importação
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def formatar_moeda(valor):
    """Formata o valor numérico como moeda brasileira (R$)."""
    return f"R$ {valor:,.2f}"

def exibir_dashboard(df):
    """Exibe o dashboard de vendas no Streamlit."""
    st.title("Dashboard de Vendas em Tempo Real")

    if df.empty:
        st.write("Nenhum dado disponível.")
        return

    # Verifica se as colunas esperadas estão presentes no DataFrame
<<<<<<< HEAD
    colunas_esperadas = ['setor', 'produto', 'número_vendas', 'valor_total_venda', 'preço', 'marca', 'localizacao']
    if not all(col in df.columns for col in colunas_esperadas):
=======
    if not all(col in df.columns for col in ['setor', 'produto', 'número_vendas', 'valor_total_venda', 'preço', 'marca', 'localizacao']):
>>>>>>> 96f366f (Primeiro commit)
        st.write("Erro: Colunas esperadas estão ausentes no arquivo CSV.")
        st.write("Colunas disponíveis:", df.columns.tolist())
        return

    # Cria duas colunas para o layout do dashboard
    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("## Visão Geral")
        
        # Produto Mais Vendido
        st.markdown("### Produto Mais Vendido")
        if 'número_vendas' in df.columns:
            df_produto_mais_vendido = df.groupby("produto").agg({"número_vendas": "sum"}).reset_index()
            df_produto_mais_vendido = df_produto_mais_vendido.sort_values(by="número_vendas", ascending=False).head(1)
            st.write(df_produto_mais_vendido)
<<<<<<< HEAD
        else:
            st.write("Sem dados para exibir.")
=======
>>>>>>> 96f366f (Primeiro commit)

        # Produto Menos Vendido
        st.markdown("### Produto Menos Vendido")
        if 'número_vendas' in df.columns:
            df_produto_menos_vendido = df.groupby("produto").agg({"número_vendas": "sum"}).reset_index()
            df_produto_menos_vendido = df_produto_menos_vendido.sort_values(by="número_vendas", ascending=True).head(1)
            st.write(df_produto_menos_vendido)
<<<<<<< HEAD
        else:
            st.write("Sem dados para exibir.")
=======
>>>>>>> 96f366f (Primeiro commit)

        # Faturamento Total
        st.markdown("### Faturamento Total")
        if 'valor_total_venda' in df.columns:
            df_faturamento_total = df.groupby("produto").agg({"valor_total_venda": "sum"}).reset_index()
            df_faturamento_total = df_faturamento_total.sort_values(by="valor_total_venda", ascending=False)
            st.write(df_faturamento_total)
        else:
            st.write("Sem dados para exibir.")

        # Cálculo do total de vendas e lucro líquido estimado
        total_vendas = df['valor_total_venda'].sum()
        lucro_liquido = 0.2 * total_vendas
        st.markdown(f"**Total de Vendas:** {formatar_moeda(total_vendas)}")
        st.markdown(f"**Lucro Líquido Estimado:** {formatar_moeda(lucro_liquido)}")

    with col2:
        st.markdown("## Métricas Adicionais")
        
        # Lucro Bruto
        st.markdown("### Lucro Bruto")
        if 'preço' in df.columns and 'número_vendas' in df.columns:
            df_lucro_bruto = df.groupby("produto").apply(
                lambda x: pd.Series({
                    "lucro_bruto": (x["valor_total_venda"].sum() - x["número_vendas"].sum() * x["preço"].mean())
                })
            ).reset_index()
            df_lucro_bruto = df_lucro_bruto.sort_values(by="lucro_bruto", ascending=True).head(1)
            st.write(df_lucro_bruto)
        else:
            st.write("Sem dados para exibir.")

        # Marca com Maior Vendas
        st.markdown("### Marca com Maior Vendas")
        if 'valor_total_venda' in df.columns:
            df_marca_maior_vendas = df.groupby("marca").agg({"valor_total_venda": "sum"}).reset_index()
            df_marca_maior_vendas = df_marca_maior_vendas.sort_values(by="valor_total_venda", ascending=False).head(1)
            st.write(df_marca_maior_vendas)
        else:
            st.write("Sem dados para exibir.")

        # Ticket Médio por Loja
        st.markdown("### Ticket Médio por Loja")
        if 'preço' in df.columns and 'número_vendas' in df.columns:
            df_ticket_medio = df.groupby("localizacao").apply(
                lambda x: pd.Series({
                    "ticket_medio": (x["valor_total_venda"].sum() / x["número_vendas"].sum()) if x["número_vendas"].sum() > 0 else 0
                })
            ).reset_index()
            df_ticket_medio = df_ticket_medio.sort_values(by="ticket_medio", ascending=False)
            df_ticket_medio["ticket_medio"] = df_ticket_medio["ticket_medio"].apply(formatar_moeda)
            st.write(df_ticket_medio)
        else:
            st.write("Sem dados para exibir.")

    st.markdown("## Filtros e Gráficos Interativos")

    # Seletor de filtro para diferentes visualizações
    filtro = st.selectbox(
        "Escolha uma visualização:",
        ["Faturamento Total da Semana por Setor", "Faturamento Total de Todas as Lojas", "Top 10 Produtos Mais Vendidos", "Top 10 Produtos Menos Vendidos"]
    )

    # Gráfico de Faturamento Total da Semana por Setor
    if filtro == "Faturamento Total da Semana por Setor":
        if 'valor_vendas_semana' in df.columns:
            df_agrupado_setor = df.groupby("setor").agg({"valor_vendas_semana": "sum"}).reset_index()
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.barplot(data=df_agrupado_setor, x="setor", y="valor_vendas_semana", palette="viridis", ax=ax)
            ax.set_xlabel("Setor")
            ax.set_ylabel("Faturamento Total da Semana")
            ax.set_title("Faturamento Total da Semana por Setor")
            st.pyplot(fig)
        else:
            st.write("Sem dados para exibir no gráfico.")

    # Gráfico de Faturamento Total de Todas as Lojas
    elif filtro == "Faturamento Total de Todas as Lojas":
        if 'valor_total_venda' in df.columns:
            df_agrupado_loja = df.groupby("localizacao").agg({"valor_total_venda": "sum"}).reset_index()
            fig, ax = plt.subplots(figsize=(8, 6))
            sns.barplot(data=df_agrupado_loja, x="localizacao", y="valor_total_venda", palette="crest", ax=ax)
            ax.set_xlabel("Loja")
            ax.set_ylabel("Faturamento Total")
            ax.set_title("Faturamento Total por Loja")
            st.pyplot(fig)
        else:
            st.write("Sem dados para exibir no gráfico.")

    # Gráfico dos 10 Produtos Mais Vendidos
    elif filtro == "Top 10 Produtos Mais Vendidos":
        if 'número_vendas' in df.columns:
            df_produto_mais_vendido = df.groupby("produto").agg({"número_vendas": "sum"}).reset_index()
            df_produto_mais_vendido = df_produto_mais_vendido.sort_values(by="número_vendas", ascending=False).head(10)
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.barplot(data=df_produto_mais_vendido, x="produto", y="número_vendas", palette="cubehelix", ax=ax)
            ax.set_xlabel("Produto")
            ax.set_ylabel("Número de Vendas")
            ax.set_title("Top 10 Produtos Mais Vendidos")
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
            st.pyplot(fig)
        else:
            st.write("Sem dados para exibir no gráfico.")

    # Gráfico dos 10 Produtos Menos Vendidos nos Últimos 30 Dias
    elif filtro == "Top 10 Produtos Menos Vendidos":
        if 'data_venda' in df.columns and 'número_vendas' in df.columns:
            data_limite = datetime.now() - timedelta(days=30)
            df_ultimos_30_dias = df[df['data_venda'] >= data_limite]
            df_produto_menos_vendido = df_ultimos_30_dias.groupby("produto").agg({"número_vendas": "sum"}).reset_index()
            df_produto_menos_vendido = df_produto_menos_vendido.sort_values(by="número_vendas", ascending=True).head(10)
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.barplot(data=df_produto_menos_vendido, x="produto", y="número_vendas", palette="plasma", ax=ax)
            ax.set_xlabel("Produto")
            ax.set_ylabel("Número de Vendas")
            ax.set_title("Top 10 Produtos que Menos Venderam nos Últimos 30 Dias")
            ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha="right")
            st.pyplot(fig)
        else:
            st.write("Sem dados para exibir no gráfico.")

def previsao_vendas(modelo, preprocessor):
    """Exibe a interface para previsão de vendas no Streamlit."""
    st.title('Previsão de Vendas')

    # Formulário para inserção de novos dados
    st.subheader('Insira novos dados para previsão')

    with st.form(key='input_form'):
<<<<<<< HEAD
        setor = st.selectbox('Setor', [''] + df['setor'].unique().tolist())  # Adiciona opção de selecionar vazio
=======
        setor = st.selectbox('Setor', df['setor'].unique())
>>>>>>> 96f366f (Primeiro commit)
        marca = st.text_input('Marca')
        preço = st.number_input('Preço', min_value=0.0)
        quantidade_estoque = st.number_input('Quantidade em Estoque', min_value=0)
        número_vendas = st.number_input('Número de Vendas', min_value=0)
        modelo_texto = st.text_input('Modelo')
        desconto = st.number_input('Desconto', min_value=0.0, max_value=1.0, step=0.01)
        fornecedor = st.text_input('Fornecedor')
        localizacao = st.text_input('Localização', '')  # Inclua a localização se necessário

        # Botão para submeter o formulário
        submit_button = st.form_submit_button(label='Prever')

        if submit_button:
            # Cria um DataFrame com os dados inseridos pelo usuário
            dados_novos = pd.DataFrame([{
                'setor': setor,
                'marca': marca,
                'preço': preço,
                'quantidade_estoque': quantidade_estoque,
                'número_vendas': número_vendas,
                'modelo': modelo_texto,
                'desconto': desconto,
                'fornecedor': fornecedor,
<<<<<<< HEAD
                'localizacao': localizacao
=======
                'localizacao': localizacao  # Inclua a coluna 'localizacao'
>>>>>>> 96f366f (Primeiro commit)
            }])

            # Codifica e transforma os dados de entrada conforme o pré-processador
            dados_novos_processed = preprocessor.transform(dados_novos)
            
            # Faz a previsão do valor total de venda
            valor_previsto = modelo.predict(dados_novos_processed)
            st.write(f'Valor total de venda previsto: {formatar_moeda(valor_previsto[0])}')

if __name__ == "__main__":
    # Carrega e prepara os dados
    df = carregar_dados('dados_vendas.csv')
    X_train, X_test, y_train, y_test, preprocessor = preparar_dados(df)
    modelo = treinar_modelo(X_train, y_train)
    mse = avaliar_modelo(modelo, X_test, y_test)

    # Configuração do menu
    st.sidebar.title("Menu")
    opcao = st.sidebar.selectbox("Escolha uma opção", ["Dashboard", "Previsão de Vendas"])

    if opcao == "Dashboard":
        exibir_dashboard(df)
    elif opcao == "Previsão de Vendas":
        previsao_vendas(modelo, preprocessor)
