import csv
import random

base_de_dados = []
with open('winequality-red.csv', 'r') as csvfile:
    dados = csv.reader(csvfile, delimiter=';')
    for line in dados:
        line = [float(i) for i in line]
        base_de_dados.append(line)


def separacao_teste_treino(base_de_dados, porcentagem_treino):
    porcento = porcentagem_treino * len(
        base_de_dados) // 100  # Neste caso, com esse banco de dados, ele está dando uma porcentagem de 1279
    data_treino = random.sample(base_de_dados, porcento) # 1279 amostras aleatórias com valores parecidos com os da base de dados
    print(data_treino)


if __name__ == '__main__':
    separacao_teste_treino(base_de_dados, 80)
