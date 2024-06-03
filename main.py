import networkx as nx

# Создаем граф с семью узлами
G = nx.Graph()
G.add_nodes_from([0, 1, 2, 3, 4, 5, 6])

# Добавляем ребра, создающие "яму" и "горбик"
G.add_edges_from([
    (0, 1), (1, 2), (2, 3), 
    (3, 4), (4, 5), (5, 6), 
    (1, 4)
])

# Вычисляем центральность узлов
centrality = nx.eigenvector_centrality_numpy(G)

# Выводим результаты
print(f"Граф: {G}")
for n in centrality:
    print(f"c({n}) = {centrality[n]:.4f}") 