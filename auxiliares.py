from datetime import date
import json
import os


# FUNÇÕES AUXILIARES %m/%d/%Y, %H:%M:%S
def pegar_data():
    data_atual = date.today()
    return data_atual.strftime("%d/%m/%Y")


# GRAVAR JSON FILE
def gravar_json(site, nome, dados):
    with open(nome, 'w', encoding="utf-8") as arquivo_saida:
        json.dump({"vagas": dados}, arquivo_saida, indent=4, ensure_ascii=False)
    
    print(f"Vagas dos Sites {site} salvas em {nome} com sucesso!")


# ATUALIZAR JSONS
def agrupar_jsons():
    # Armazenadores
    nomes_arquivos = []
    dados = []
    # Lista o nomes dos arquivos
    for root, dirs, files in os.walk('resultados'):
        for name in files:
            if name != 'vagas.json':
                file = os.path.join(root, name)
                nomes_arquivos.append(file)
    # Lê os arquivos e armazena os dados em uma lista
    for nome in nomes_arquivos:
        with open(nome, "r", encoding="utf-8") as arquivo:
            dados.extend(json.load(arquivo)['vagas'])
    # Escreve os dados no arquivo de saída
    with open('resultados/vagas.json', 'w+', encoding="utf-8") as arquivo_saida:
        json.dump({"vagas": dados}, arquivo_saida, indent=4, ensure_ascii=False)
    print("JSons atualizados")
