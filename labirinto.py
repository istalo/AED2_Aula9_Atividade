labirinto = [
    "I.#.######",
    "....#.####",
    "..#....###",
    "#.#.##...#",
    "#...#.#...",
    "#.#..#..#.",
    "#.#..F.##.",
    ".##.##.###",
    ".#.#..####",
    "##.#######",
]

def achar(lab, simbolo):
    for i, linha in enumerate(lab):
        if simbolo in linha:
            return (i, linha.index(simbolo))
inicio = achar(labirinto, 'I')   # (0, 0)
saida  = achar(labirinto, 'F')   # (6, 5)

DIRECOES = [(-1, 0), (0, 1), (1, 0), (0, -1)]   # ↑ → ↓ ←

def livre(lab, i, j):
    dentro = 0 <= i < len(lab) and 0 <= j < len(lab[0])
    return dentro and lab[i][j] != '#'

def montar_grafo(lab):
    grafo = {}
    for i in range(len(lab)):
        for j in range(len(lab[0])):
            if not livre(lab, i, j):
                continue
            grafo[(i, j)] = []
            for di, dj in DIRECOES:
                if livre(lab, i + di, j + dj):
                    grafo[(i, j)].append((i + di, j + dj))
    return grafo
grafo = montar_grafo(labirinto)

def dfs(grafo, atual, saida, visitados=None):
    if visitados is None:
        visitados = set()
    visitados.add(atual)
    if atual == saida:
        return [atual]
    for vizinho in grafo[atual]:
        if vizinho not in visitados:
            caminho = dfs(grafo, vizinho, saida, visitados)
            if caminho:
                return [atual] + caminho
    return []

from collections import deque

def bfs(grafo, inicio, saida):
    visitados = {inicio}
    fila = deque([(inicio, [inicio])])
    while fila:
        atual, caminho = fila.popleft()
        if atual == saida:
            return caminho
        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append((vizinho, caminho + [vizinho]))
    return []

import heapq

def h(v, saida):
    return abs(v[0] - saida[0]) + abs(v[1] - saida[1])

def gulosa(grafo, inicio, saida):
    fronteira = [(h(inicio, saida), inicio)]
    veio = {inicio: None}
    while fronteira:
        _, v = heapq.heappop(fronteira)
        if v == saida:
            break
        for w in grafo[v]:
            if w not in veio:
                veio[w] = v
                heapq.heappush(fronteira, (h(w, saida), w))
    if saida not in veio:
        return []
    caminho = []
    atual = saida
    while atual is not None:
        caminho.append(atual)
        atual = veio[atual]
        
    return caminho[::-1]

def desenhar(lab, caminho):
    grade = [list(linha) for linha in lab]
    for i, j in caminho:
        if grade[i][j] == '.':
            grade[i][j] = '*'
    for linha in grade:
        print(''.join(linha))

caminho_dfs = dfs(grafo, inicio, saida)
print("Caminho encontrado pelo DFS:")
desenhar(labirinto, caminho_dfs)

caminho_bfs = bfs(grafo, inicio, saida)
print("Caminho encontrado pelo BFS:")
desenhar(labirinto, caminho_bfs)

caminho_gulosa = gulosa(grafo, inicio, saida)
print("Caminho encontrado pela Busca Gulosa:")
desenhar(labirinto, caminho_gulosa)