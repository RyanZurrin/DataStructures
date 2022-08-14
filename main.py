import graph

g = graph.Graph(13, directed=True, weighted=True)

g.add_edge(0, 1, 4)
g.add_edge(0, 2, 3)
g.add_edge(1, 2, 1)
g.add_edge(1, 3, 2)
g.add_edge(2, 0, 6)
g.add_edge(2, 3, 2)
g.add_edge(3, 8, 1)
g.add_edge(3, 3, 3)
g.add_edge(3, 4, 9)
g.add_edge(4, 3, 3)
g.add_edge(4, 5, 1)
g.add_edge(5, 6, 2)
g.add_edge(6, 7, 1)
g.add_edge(7, 8, 8)
g.add_edge(8, 9, 2)
g.add_edge(9, 10, 11)
g.add_edge(10, 11, 1)
g.add_edge(11, 12, 1)
g.add_edge(12, 9, 1)
g.add_edge(12, 10, 1)
g.add_edge(12, 11, 12)
g.add_edge(12, 12, 1)

g.print_graph()
g.print_adj_matrix()

print(g.shortest_path(0, 12))
print(g.is_connected())
print(g.is_bipartite())

g.bfs(0)

print()

g.dfs(0)

print()
distances = g.dijkstra(2)

