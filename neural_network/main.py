from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

# Exemplos utilizando porcos e cachorros

# Possui pelo Longo? [0 ou 1] ou [False ou True]

# Posui perna curta? [0 ou 1] ou [False ou True]

# Faz auau? [0 ou 1] ou [False ou True]

porco1 = [0, 1, 0]
porco2 = [0, 1, 1]
porco3 = [1, 1, 0]

cachorro1 = [0, 1, 1]
cachorro2 = [1, 0, 1]
cachorro3 = [1, 1, 1]

treino_x = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]
# No caso dados de treino(treino_x) são as variaveis que eu apresentaria para alguem que estou ensinando, neste caso um IA, e que a partir destes dados
# ele irá aprender a reconhecer um porco de um cachorro

treino_y = [1, 1, 1, 0, 0, 0]  # No caso os porcos representam o número 1 e os cachorros o número 0
# No caso a IA erá pegar este 1 e 0 e irá compara-los com o treino_x, e irá aprender a reconhecer um porco de um cachorro

Modelo = LinearSVC()  # Criando um modelo de IA

Modelo.fit(treino_x, treino_y)  # Treinando o modelo de IA
teste_x = [0, 1, 1]  # No caso este animal é um cachorro

resp = Modelo.predict([teste_x])
test_y = [0]  # No caso os porcos representam o número 1 e os cachorros o número 0
accuracy = accuracy_score(test_y, resp)

# Testando o modelo de IA
for i in resp:
    if i == 1:
        print("Porco")
    else:
        print("Cachorro")
print(f"Precisão: {accuracy * 100:.2f}%")  # Mostrando a precisão do modelo de IA

teste_x = [[1, 1, 1], [1, 1, 0],  # No caso este animal é um cachorro
           [0, 1, 1]]
teste_y = [0, 1, 0]  # No caso os porcos representam o número 1 e os cachorros o número 0
resp = Modelo.predict(teste_x)  # Testando o modelo de IA
print("/ ---------- /")
for i in resp:
    if i == 1:
        print("Porco")
    else:
        print("Cachorro")

accuracy = accuracy_score(teste_y, resp)  # Calculando a precisão do modelo de IA
print(f"Precisão: {accuracy * 100:.2f}%")  # Mostrando a precisão do modelo de IA
