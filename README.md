# Real-Time-Sales-Visualization-Prediction-Streamlit
Plataforma para monitorar e prever vendas com integração de dados e visualizações interativas. | Automatiza processos.  Análise detalhada. Escalabilidade | Scripts:  app.py: Dashboard e previsão. data_preparation.py: Prepara dados. model_training.py: Treina o modelo. Databasesqlite.py: Gerencia banco de dados.

### Projeto: Sistema de Visualização e Previsão de Vendas

**Objetivo:**
Desenvolver um sistema completo para a visualização e previsão de vendas que integra a coleta de dados, preparação, treinamento de modelos e visualização em tempo real, utilizando o Streamlit para interação com o usuário.

**Público-alvo:**
Empresas e analistas de dados que buscam uma solução integrada para monitorar e prever o desempenho de vendas, proporcionando insights valiosos e previsões precisas para otimização de estratégias comerciais.

**Vantagens em Relação aos Processos Padrões:**
- **Integração Completa:** Combina coleta, armazenamento, preparação e visualização de dados em uma única plataforma.
- **Previsão Precisa:** Utiliza modelos de regressão treinados para prever vendas futuras com base em dados reais.
- **Visualização Interativa:** Oferece gráficos e dashboards interativos que facilitam a análise e interpretação dos dados.

**Vantagens de Utilizar o Sistema:**
- **Eficiência Operacional:** Automatiza a coleta e análise de dados, reduzindo o tempo gasto em tarefas manuais.
- **Insights Aprofundados:** Proporciona uma visão detalhada das vendas e previsões precisas para tomada de decisões estratégicas.
- **Flexibilidade:** Permite personalização e escalabilidade de acordo com as necessidades específicas do negócio.

**Escalabilidade:**
O sistema é escalável, permitindo a adição de novas funcionalidades, integração com outras fontes de dados e ajuste para lidar com maiores volumes de informações conforme a empresa cresce.

**Tempo Necessário:**
- **Configuração Inicial:** Aproximadamente 2-4 horas para a configuração completa e personalização do sistema.
- **Operação Contínua:** Atualização e visualização contínuas com dados em tempo real.

---

**Scripts e Funções Principais:**

1. **app.py**
   - **Descrição:** O núcleo da aplicação que oferece um dashboard interativo para visualização de vendas e uma funcionalidade de previsão de vendas usando um modelo treinado.
   - **Funções Principais:**
     - **formatar_moeda(valor):** Formata números como moeda brasileira (R$).
     - **exibir_dashboard(df):** Apresenta métricas de vendas e gráficos interativos.
     - **previsao_vendas(modelo, preprocessor):** Permite prever o valor total das vendas com base em novos dados.

2. **data_preparation.py**
   - **Descrição:** Prepara os dados para treinamento do modelo, incluindo a imputação de valores ausentes e a codificação de variáveis categóricas.
   - **Funções Principais:**
     - **carregar_dados(arquivo_csv):** Carrega dados de um arquivo CSV e processa a coluna de datas.
     - **preparar_dados(df):** Realiza a imputação de dados faltantes, codificação one-hot e divisão dos dados em conjuntos de treinamento e teste.

3. **model_training.py**
   - **Descrição:** Responsável pelo treinamento e avaliação do modelo de regressão linear para prever o valor das vendas.
   - **Funções Principais:**
     - **treinar_modelo(X_train, y_train):** Treina o modelo de regressão linear com dados de treinamento.
     - **avaliar_modelo(modelo, X_test, y_test):** Avalia o modelo treinado e calcula o erro quadrático médio (MSE).

4. **Databasesqlite.py**
   - **Descrição:** Gerencia a criação e manutenção de um banco de dados SQLite para armazenar dados de vendas, além de permitir a atualização periódica dos dados.
   - **Funções Principais:**
     - **gerar_dados_aleatorios():** Gera uma entrada de venda com dados aleatórios para simulação.
     - **criar_tabela():** Cria uma tabela no banco de dados SQLite para armazenar as vendas.
     - **adicionar_dados_db(dados):** Adiciona uma entrada de venda ao banco de dados.
     - **adicionar_dados_csv_e_db(arquivo_csv):** Adiciona dados tanto ao arquivo CSV quanto ao banco de dados.
     - **atualizar_dados_periodicamente(arquivo_csv, intervalo):** Atualiza periodicamente os dados no CSV e no banco de dados.

Cada script é projetado para contribuir de maneira específica ao fluxo geral da aplicação, assegurando que os dados sejam corretamente preparados, armazenados e analisados para fornecer insights valiosos e previsões precisas.
