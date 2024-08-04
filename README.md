## Faala dev, Lucas Aqui!

<div>
  <img height="180em" src="https://github-readme-stats.vercel.app/api?username=Desenvolvedorpythonanalista&show_icons=true&theme=great-gatsby&include_all_commits=true&count_private=true"/>
  <img align="right" height="180em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Desenvolvedorpythonanalista&layout=compact&langs_count=16&theme=great-gatsby"/>
</div>
<br>

<div align="center"> 
  <div style="display: inline_block"><br>
    <img align="left" height="250" alt="coding-time" src="code.gif">
    <h1 align="center">Melhores Tecnologias <3</h1>
    <!-- Ícones das Tecnologias -->
    <img align="center" height="30" width="40" alt="python-icon" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">
    <img align="center" height="30" width="40" alt="django-icon" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-original.svg">
    <img align="center" height="30" width="40" alt="mysql-icon" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original.svg">
    <img align="center" height="30" width="40" alt="nodejs-icon" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/nodejs/nodejs-original.svg">
    <img align="center" height="30" width="40" alt="streamlit-icon" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/streamlit/streamlit-original.svg">
   </div>
    
  <h1 align="center">Redes Sociais</h1>
    <a href="mailto:lachimolalala61@gmail.com">
      <img width="30" src="https://upload.wikimedia.org/wikipedia/commons/4/4e/Gmail_Icon.png" alt="gmail">
    </a>
    <a href="https://www.linkedin.com/in/miguel-lucas-60091119b/">
      <img width="25" src="https://upload.wikimedia.org/wikipedia/commons/0/01/LinkedIn_Logo_2013.png" alt="linkedin">
    </a>
    <a href="https://www.youtube.com/channel/UCd5Ivcm28R1C3fCQKbOx2cg">
      <img width="35" src="https://upload.wikimedia.org/wikipedia/commons/4/42/YouTube_icon_%282013-2017%29.png" alt="youtube">
    </a>
    <a href="https://www.instagram.com/devparadev/">
      <img width="25" src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="instagram">
    </a>
</div>
  
![Snake animation](https://github.com/LuigiGF/LuigiGF/blob/output/github-contribution-grid-snake.svg)





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

<h1 align="center">Awesome GitHub Profile README
<a href="https://www.producthunt.com/posts/awesome-github-profiles?utm_source=badge-featured&utm_medium=badge&utm_souce=badge-awesome-github-profiles" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=277987&theme=light" alt="Awesome GitHub Profiles - Best curated list of developers readme, updated every 15 min | Product Hunt" style="width: 200px; height: 44px;" width="200" height="44" /></a></h1>
<div align="center">
<img src="https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg" alt="Awesome Badge"/>
<a href="https://arbeitnow.com/?utm_source=awesome-github-profile-readme"><img src="https://img.shields.io/static/v1?label=&labelColor=505050&message=arbeitnow&color=%230076D6&style=flat&logo=google-chrome&logoColor=%230076D6" alt="website"/></a>
<!-- <img src="http://hits.dwyl.com/abhisheknaiidu/awesome-github-profile-readme.svg" alt="Hits Badge"/> -->
<img src="https://img.shields.io/static/v1?label=%F0%9F%8C%9F&message=If%20Useful&style=style=flat&color=BC4E99" alt="Star Badge"/>
<a href="https://discord.gg/XTW52Kt"><img src="https://img.shields.io/discord/733027681184251937.svg?style=flat&label=Join%20Community&color=7289DA" alt="Join Community Badge"/></a>
<a href="https://twitter.com/abhisheknaiidu" ><img src="https://img.shields.io/twitter/follow/abhisheknaiidu.svg?style=social" /> </a>
<br>

<i>A curated list of awesome Github Profile READMEs</i>

<a href="https://github.com/abhisheknaiidu/awesome-github-profile-readme/stargazers"><img src="https://img.shields.io/github/stars/abhisheknaiidu/awesome-github-profile-readme" alt="Stars Badge"/></a>
<a href="https://github.com/abhisheknaiidu/awesome-github-profile-readme/network/members"><img src="https://img.shields.io/github/forks/abhisheknaiidu/awesome-github-profile-readme" alt="Forks Badge"/></a>
<a href="https://github.com/abhisheknaiidu/awesome-github-profile-readme/pulls"><img src="https://img.shields.io/github/issues-pr/abhisheknaiidu/awesome-github-profile-readme" alt="Pull Requests Badge"/></a>
<a href="https://github.com/abhisheknaiidu/awesome-github-profile-readme/issues"><img src="https://img.shields.io/github/issues/abhisheknaiidu/awesome-github-profile-readme" alt="Issues Badge"/></a>
<a href="https://github.com/abhisheknaiidu/awesome-github-profile-readme/graphs/contributors"><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/abhisheknaiidu/awesome-github-profile-readme?color=2b9348"></a>
<a href="https://github.com/abhisheknaiidu/awesome-github-profile-readme/blob/master/LICENSE"><img src="https://img.shields.io/github/license/abhisheknaiidu/awesome-github-profile-readme?color=2b9348" alt="License Badge"/></a>

<img alt="Awesome GitHub Profile Readme" src="assets/agpr.gif"> </img>

<i>Loved the project? Please consider [donating](https://paypal.me/abhisheknaiidu) to help it improve!</i>

</div>
