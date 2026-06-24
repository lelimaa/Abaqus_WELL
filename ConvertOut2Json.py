import csv
import json

# 1. Definimos a estrutura base do JSON que queremos gerar
dados_json = {
    "nome_experimento": "Stresses Cement",
    "unidades": {
        "tempo": "s",          # Substitua pela unidade de tempo do seu experimento
        "deslocamento": "Pa"   # Substitua pela unidade da segunda coluna (ex: Tensão/Stress)
    },
    "dados": {
        "tempo": [],
        "deslocamento": []
    }
}

# 2. Abrimos o CSV para leitura
# O parâmetro delimiter=';' é fundamental, pois seu arquivo usa ponto e vírgula
with open('StressesCementNew.csv', 'r', encoding='utf-8') as arquivo_csv:
    leitor = csv.reader(arquivo_csv, delimiter=';')
    
    # 3. Lemos o arquivo linha por linha
    for linha in leitor:
        # Verifica se a linha tem as duas colunas principais e não está vazia
        if len(linha) >= 2 and linha[0].strip() != '':
            try:
                # Extrai as duas primeiras colunas e converte para decimal (float)
                # O Python já entende notações como '4.48E+07' automaticamente
                t = float(linha[0])
                d = float(linha[1])
                
                # Adiciona os valores nas respectivas listas do dicionário
                dados_json["dados"]["tempo"].append(t)
                dados_json["dados"]["deslocamento"].append(d)
            except ValueError:
                # Se a linha contiver algum texto (como um cabeçalho), o erro é ignorado
                continue

# 4. Salvamos o dicionário preenchido em um novo arquivo JSON
with open('dados_convertidos.json', 'w', encoding='utf-8') as arquivo_json:
    # O indent=4 garante que o JSON fique quebrado em linhas e indentado
    json.dump(dados_json, arquivo_json, indent=4)

print("Conversão concluída com sucesso! Arquivo 'dados_convertidos.json' gerado.")