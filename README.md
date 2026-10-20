# Atividade Aula 9 de AED2 - Labirinto com DFS, BFS e Busca Gulosa

A atividade implementa e compara três algoritmos de busca em grafos (**DFS - Busca em Profundidade**, **BFS - Busca em Largura** e **Greedy Best-First Search - Busca Gulosa**) aplicados para resolver um labirinto 10×10 em Python.

## 1. O Labirinto Desenvolvido

O labirinto possui dimensão 10×10, onde:
- O `I` representa o **Início** em `(0, 0)`.
- O `F` representa o **Fim (Saída)** em `(6, 5)`.
- Os `#` representam as paredes do labirinto.
- Os `.` representam o caminho livre para percorrer.

O mapa foi "desenhado à mão" e conta com bifurcações (`(1,3)`/`(2,3)`) que separam dois caminhos possíveis até a saída: um pelo **centro** (mais curto, usado pela BFS e Gulosa) e um pela **direita** (mais longo, escolhido pela DFS por causa da ordem de exploração ↑ → ↓ ←). Também possui becos sem saída e células impossíveis de se alcançar.

## 2. Implementações

O labirinto é convertido em um grafo representado por lista de adjacência (dicionário em Python), onde cada tupla `(linha, coluna)` livre se conecta aos seus vizinhos ortogonais válidos.

1. **DFS:** Implementada de forma recursiva com um `set` de nós visitados. Ela explora uma direção até o fim antes de fazer *backtracking*.
2. **BFS:** Implementada com fila (`collections.deque`) em que cada item guarda o nó atual e o caminho percorrido até ele. Ela explora o labirinto em camadas para garantir o menor caminho.
3. **Busca Gulosa:** Implementada com fila de prioridade (`heapq`) e dicionário de predecessores (`veio`) para reconstruir o caminho. Ela usa a distância de Manhattan como heurística ($h(v) = |x_v - x_{saida}| + |y_v - y_{saida}|$) e sempre expande o nó que parece mais próximo da saída para ela.

## 3. Como rodar

O código usa apenas a biblioteca padrão do Python (`collections` e `heapq`), então não precisa instalar nada além do **Python 3.8+**.

1. Clone o repositório e entre na pasta:

```bash
   git clone https://github.com/istalo/AED2_Aula9_Atividade.git
```
2. Entre na pasta
```bash
    cd AED2_Aula9_Atividade
```

3. Execute o script:

```bash
   python labirinto.py
```

O script imprime o labirinto com o caminho encontrado por cada algoritmo (marcado com `*`) e mostra a tabela comparativa com o tamanho do caminho e o número de casas visitadas ao final.

## 4. Resultados Obtidos e Tabela Comparativa

Após executar o script, nota-se que os três algoritmos encontram as seguintes rotas até a saída `F`:

| Algoritmo | Tamanho do Caminho (casas) | Casas Visitadas | Garante Menor Caminho? |
| :--- | :---: | :---: | :---: |
| **DFS** | 18 | 24 | Não |
| **BFS** | 12 | 31 | Sim |
| **Busca Gulosa** | 12 | 17 | Não* |

*A gulosa achou o melhor caminho nesse labirinto, mas isso não é garantido no geral.