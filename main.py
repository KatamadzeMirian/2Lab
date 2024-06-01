import networkx as nx

def find_nodes_with_pit_and_peak(graph, centrality_measure):
  """
  Находит узлы с "ямой" и "горбиком" в распределении центральности.

  Args:
      graph: Граф NetworkX.
      centrality_measure: Функция NetworkX для расчета центральности.

  Returns:
      Список узлов с "ямой" и "горбиком".
  """

  centrality = centrality_measure(graph)
  nodes_with_pit_and_peak = []

  for node in centrality:
    # Получаем значения центральности для соседей узла
    neighbors_centrality = [centrality[neighbor] for neighbor in graph.neighbors(node)]
    # Проверяем, есть ли "яма" и "горбик"
    if min(neighbors_centrality) < centrality[node] < max(neighbors_centrality):
      nodes_with_pit_and_peak.append(node)

  return nodes_with_pit_and_peak

# Пример использования:
graph = nx.karate_club_graph()  # Загружаем граф Карате-клуба
nodes_with_pit_and_peak = find_nodes_with_pit_and_peak(graph, nx.degree_centrality)
print("Узлы с \"ямой\" и \"горбиком\" по степени центральности:", nodes_with_pit_and_peak)

# Можно использовать другие типы центральности:
nodes_with_pit_and_peak = find_nodes_with_pit_and_peak(graph, nx.betweenness_centrality)
print("Узлы с \"ямой\" и \"горбиком\" по центральности посредничества:", nodes_with_pit_and_peak)