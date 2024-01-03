from queue import PriorityQueue
from pyamaze import maze, agent

destino = (1, 1)


def h_score(celula, destino):
    xlin = celula[0]
    ylin = celula[1]
    xcol = destino[0]
    ycol = destino[1]
    return abs(xlin - xcol) + abs(ylin - ycol)


def aStar(labirinto):
    # Criar tabuleiro com todos os quadrados com valor infinito.
    f_score = {celula: float("inf") for celula in labirinto.grid}
    g_score = {}
    # Calcular o valor da celula inicial e celulas ao redor.
    celula_inicial = (labirinto.rows, labirinto.cols)
    g_score[celula_inicial] = 0
    f_score[celula_inicial] = g_score[celula_inicial] + h_score(celula_inicial, destino)
    print(f_score)

    fila = PriorityQueue()
    item = (f_score[celula_inicial], h_score(celula_inicial, destino), celula_inicial)
    fila.put(item)

    caminho = {}
    while not fila.empty():
        celula = fila.get()[2]

        if celula == destino:
            break

        for direcao in "NSEW":
            if labirinto.maze_map[celula][direcao] == 1:
                linha = celula[0]
                coluna = celula[1]
                if direcao == "N":
                    proxima_cel = (linha - 1, coluna)
                elif direcao == "S":
                    proxima_cel = (linha + 1, coluna)
                elif direcao == "E":
                    proxima_cel = (linha, coluna + 1)
                elif direcao == "W":
                    proxima_cel = (linha, coluna - 1)

                novo_g_score = g_score[celula] + 1
                novo_f_score = novo_g_score + h_score(proxima_cel, destino)

                if novo_f_score < f_score[proxima_cel]:
                    f_score[proxima_cel] = novo_f_score
                    g_score[proxima_cel] = novo_g_score
                    item = (novo_f_score, h_score(proxima_cel, destino), proxima_cel)
                    fila.put(item)
                    caminho[proxima_cel] = celula
    caminho_final = {}
    celula_analisada = destino
    print("Celulas analisadas", len(caminho.keys()))
    while celula_analisada != celula_inicial:
        caminho_final[caminho[celula_analisada]] = celula_analisada
        celula_analisada = caminho[celula_analisada]
    return caminho_final


labirinto = maze(10, 10)
labirinto.CreateMaze()

agente = agent(labirinto, filled=True, footprints=True)
caminho = aStar(labirinto)
print(caminho)
labirinto.tracePath({agente: caminho}, delay=10)

labirinto.run()
