"""
Resumo das Funções:

gerar_dados_aleatorios(): Cria uma entrada de venda com dados aleatórios baseados em listas e dicionários fornecidos.
criar_tabela(): Cria uma tabela no banco de dados SQLite para armazenar as informações das vendas.
adicionar_dados_db(dados): Insere os dados gerados na tabela do banco de dados.
adicionar_dados_csv_e_db(arquivo_csv): Adiciona os dados gerados tanto ao arquivo CSV quanto ao banco de dados.
atualizar_dados_periodicamente(arquivo_csv, intervalo): Adiciona novos dados periodicamente (a cada 20 segundos por padrão) ao arquivo CSV e ao banco de dados.
"""

import pandas as pd
import random
import time
import os
from datetime import datetime, timedelta
import sqlite3

# Lista de fornecedores com nomes específicos
fornecedores = [
    "Distribuidora Alpha", "Importadora Beta", "Fornecedora Gamma", "Suprimentos Delta",
    "Produtos Epsilon", "Acessórios Zeta", "Mercadorias Eta", "Comércio Theta",
    "Logística Iota", "Armazém Kappa", "Venda Lambda", "Inovações Mu",
    "Comercial Nu", "Equipamentos Xi", "Serviços Omicron", "Distribuição Pi",
    "Fornecedora Rho", "Suprimentos Sigma", "Importadora Tau", "Armazém Upsilon"
]

# Lista de marcas
marcas = [
    "TechNova", "ElectroMart", "SuperGadgets", "HomeEssentials",
    "EcoWare", "PrimeProducts", "InnovateTech", "QualityGoods",
    "MegaBrand", "FutureTech", "BrightChoice", "GigaStore", 
    "SmartBuy", "NextGenProducts", "EliteElectronics", "ValueLine",
    "OptimaGoods", "SmartChoice", "Trendsetter", "ProLine"
]

# Lista de setores
setores = [
    "Eletrônicos", "Eletrodomésticos", "Móveis", "Roupas", 
    "Brinquedos", "Beleza", "Esportes", "Automotivo", 
    "Saúde", "Alimentos"
]

# Lista de produtos diferenciados por setor
produtos_por_setor = {
    "Eletrônicos": [
        "Smartphone Galaxy S21", "Smartphone iPhone 13", "Tablet iPad Pro", "Smartwatch Galaxy Watch 4",
        "Fone de Ouvido AirPods", "Notebook Dell XPS 13", "Notebook MacBook Air", "Monitor UltraWide 34''",
        "TV LED 55''", "Projetor Epson Home Cinema", "Console PlayStation 5", "Console Xbox Series X",
        "Câmera Canon EOS R5", "Câmera Sony Alpha 7", "Impressora HP DeskJet", "Impressora Epson EcoTank",
        "Teclado Mecânico Razer", "Mouse Logitech MX Master", "Câmera de Segurança Arlo", "Drone DJI Mavic"
    ],
    "Eletrodomésticos": [
        "Geladeira Samsung Frost Free", "Máquina de Lavar Brastemp", "Fogão Electrolux", "Micro-ondas Panasonic",
        "Aspirador de Pó Philips", "Ar Condicionado LG", "Secadora de Roupas Whirlpool", "Cafeteira Nespresso",
        "Lavadora de Roupas LG", "Forno de Embutir Brastemp", "Liquidificador Oster", "Batedeira KitchenAid",
        "Torradeira Philips", "Purificador de Água Consul", "Ventilador Mondial", "Aquecedor Cadence",
        "Frigobar Electrolux", "Máquina de Café Expresso DeLonghi", "Desumidificador Britânia", "Espremedor de Frutas Hamilton Beach"
    ],
    "Móveis": [
        "Sofá Retrátil 3 Lugares", "Mesa de Jantar 6 Lugares", "Cadeira de Escritório Ergonômica", "Rack para TV",
        "Cama Box King Size", "Guarda-Roupa 6 Portas", "Estante para Livros", "Mesa de Centro", "Cômoda 5 Gavetas",
        "Poltrona Reclinável", "Mesa de Escritório", "Criado-Mudo", "Painel para TV", "Banco de Jardim",
        "Armário de Cozinha", "Sofá de Canto", "Mesa de Cabeceira", "Cadeira de Escritório com Rodízios",
        "Mesa de Café com 2 Puffs", "Cama Infantil"
    ],
    "Roupas": [
        "Camiseta Masculina Básica", "Camisa Social Feminina", "Vestido Longo Estampado", "Calça Jeans Masculina",
        "Jaqueta de Couro", "Blusa de Frio Tricot", "Saia Midi", "Shorts Esportivo", "Camisa Polo", "Macacão Jeans",
        "Suéter de Lã", "Vestido Casual", "Camiseta de Banda", "Calça de Moletom", "Camiseta de Manga Longa",
        "Camisa de Flanela", "T-shirt Básica", "Blusa de Seda", "Calça Legging", "Casaco de Inverno"
    ],
    "Brinquedos": [
        "Boneca Barbie Fashion", "Carrinho Hot Wheels", "Blocos de Montar LEGO", "Trenzinho Elétrico", "Pelúcia Ursinho",
        "Quebra-Cabeça 1000 Peças", "Jogo de Tabuleiro Monopoly", "Boneco Star Wars", "Carrinho de Controle Remoto",
        "Jogo Educativo para Crianças", "Boneca de Pano", "Trampolim Infantil", "Estação de Brinquedos",
        "Livros Infantis", "Kits de Arte", "Robô Educativo", "Jogo de Vídeo Game para Crianças", "Bicicleta Infantil",
        "Arco e Flecha de Brinquedo", "Playmobil Aventuras"
    ],
    "Beleza": [
        "Creme Anti-Idade L'Oréal", "Máscara Facial Neutrogena", "Perfume Chanel No. 5", "Shampoo Head & Shoulders",
        "Condicionador Pantene", "Creme Hidratante Nivea", "Lápis de Olho Maybelline", "Base Vult", "Blush MAC",
        "Protetor Solar La Roche-Posay", "Esfoliante Facial Avon", "Hidratante para Corpo Natura", "Colônia Infantil",
        "Desodorante Rexona", "Creme para Mãos Granado", "Água Micelar Garnier", "Máscara de Cílios Dior",
        "Perfume Dolce & Gabbana", "Kit de Maquiagem O Boticário", "Creme para o Rosto Clinique"
    ],
    "Esportes": [
        "Raquete de Tênis Wilson", "Bola de Futebol Nike", "Tênis de Corrida Asics", "Camiseta de Futebol Adidas",
        "Bola de Basquete Spalding", "Luvas de Boxe Everlast", "Saco de Boxe", "Kit de Natação Speedo", "Canoe Kayak",
        "Bicicleta Mountain Bike", "Tênis de Basquete Converse", "Patins Rollerblade", "Bola de Vôlei Mizuno",
        "Cadeira de Camping", "Mochila de Trekking", "Tenda para Acampamento", "Colchonete para Yoga", "Acessórios para Escalada",
        "Cordas de Escalada", "Kit de Pesca"
    ],
    "Automotivo": [
        "Óleo de Motor Mobil 1", "Cera para Carro Turtle Wax", "Filtro de Ar K&N", "Lâmpada de Farol Philips",
        "Bateria de Carro Varta", "Tapete para Carro", "Porta-Copos Automotivo", "Mala de Viagem", "Capa de Banco",
        "Protetor Solar para Carro", "Limpador de Parabrisa", "Kit de Ferramentas Automotivas", "Cabo de Ignição NGK",
        "Antena para Carro", "Alarmes e Sensores", "Suporte para Celular", "Calotas para Roda", "Rodas Esportivas",
        "Desembassador de Parabrisa", "Cobertura para Carro"
    ],
    "Saúde": [
        "Vitaminas C + D", "Termômetro Digital", "Medicamento Para Dor", "Desinfetante Antisséptico", "Protetor Solar",
        "Kit de Primeiros Socorros", "Pomada para Cortes", "Repelente de Insetos", "Antialérgico", "Suplemento de Ferro",
        "Escova de Dentes Elétrica", "Cinta Abdominal", "Creme para Massagem", "Máscara Facial", "Pasta de Dente",
        "Solução Salina", "Curativos Esterilizados", "Suplemento de Ômega 3", "Desodorante Antibacteriano", "Antisséptico Bucal"
    ],
    "Alimentos": [
        "Arroz Integral", "Feijão Preto", "Açúcar Demerara", "Café em Grãos", "Óleo de Soja", "Macarrão Integral",
        "Leite Longa Vida", "Margarina", "Biscoito Integral", "Sopa enlatada", "Molho de Tomate", "Suco de Laranja",
        "Farinha de Trigo", "Chocolate em Pó", "Cereal Matinal", "Salgadinhos", "Azeite Extra Virgem", "Manteiga",
        "Pasta de Amendoim", "Tempero Pronto"
    ]
}

def gerar_dados_aleatorios():
    """
    Gera uma entrada de venda com dados aleatórios.
    """
    data_venda = (datetime.now() - timedelta(days=random.randint(1, 365))).strftime('%Y-%m-%d')
    fornecedor = random.choice(fornecedores)
    marca = random.choice(marcas)
    setor = random.choice(setores)
    produto = random.choice(produtos_por_setor[setor])
    valor = round(random.uniform(10, 1000), 2)
    quantidade = random.randint(1, 10)
    total = round(valor * quantidade, 2)

    return {
        "Data da Venda": data_venda,
        "Fornecedor": fornecedor,
        "Marca": marca,
        "Setor": setor,
        "Produto": produto,
        "Valor Unitário": valor,
        "Quantidade": quantidade,
        "Total": total
    }

def criar_tabela():
    """
    Cria uma tabela no banco de dados SQLite para armazenar as informações das vendas.
    """
    conn = sqlite3.connect('vendas.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vendas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_venda TEXT,
            fornecedor TEXT,
            marca TEXT,
            setor TEXT,
            produto TEXT,
            valor_unitario REAL,
            quantidade INTEGER,
            total REAL
        )
    ''')
    conn.commit()
    conn.close()

def adicionar_dados_db(dados):
    """
    Insere os dados gerados na tabela do banco de dados.
    """
    conn = sqlite3.connect('vendas.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO vendas (data_venda, fornecedor, marca, setor, produto, valor_unitario, quantidade, total)
        VALUES (:Data da Venda, :Fornecedor, :Marca, :Setor, :Produto, :Valor Unitário, :Quantidade, :Total)
    ''', dados)
    conn.commit()
    conn.close()

def adicionar_dados_csv_e_db(arquivo_csv):
    """
    Adiciona os dados gerados tanto ao arquivo CSV quanto ao banco de dados.
    """
    dados = gerar_dados_aleatorios()
    
    # Adicionar ao CSV
    if not os.path.exists(arquivo_csv):
        df = pd.DataFrame([dados])
        df.to_csv(arquivo_csv, index=False)
    else:
        df = pd.read_csv(arquivo_csv)
        df = df.append(dados, ignore_index=True)
        df.to_csv(arquivo_csv, index=False)
    
    # Adicionar ao banco de dados
    adicionar_dados_db(dados)

def atualizar_dados_periodicamente(arquivo_csv, intervalo=20):
    """
    Adiciona novos dados periodicamente (a cada intervalo de segundos) ao arquivo CSV e ao banco de dados.
    """
    criar_tabela()
    while True:
        adicionar_dados_csv_e_db(arquivo_csv)
        time.sleep(intervalo)

if __name__ == "__main__":
    atualizar_dados_periodicamente('vendas.csv')
