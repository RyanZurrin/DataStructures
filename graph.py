# class to represent a graph
import heapq


class Node:
    def __init__(self, data, weight):
        self.data = data
        self.weight = weight
        self.next = None


class Graph:
    def __init__(self, vertices, directed=False, weighted=False):
        self.V = vertices
        self.graph = [None] * self.V
        self.adj = [[] for _ in range(self.V)]
        self.E = 0
        self.is_directed = directed
        self.is_weighted = weighted

    def add_edge(self, src, dest, weight=1):
        node = Node(dest, weight)
        node.next = self.graph[src]
        self.graph[src] = node
        self.adj[src].append(dest)
        self.E += 1
        if not self.is_directed:
            node = Node(src, weight)
            node.next = self.graph[dest]
            self.graph[dest] = node
            self.adj[dest].append(src)
            self.E += 1

    def print_graph(self):
        for i in range(self.V):
            print("Adjacency list of vertex {}\n head".format(i), end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.data), end="")
                temp = temp.next
            print(" \n")

    def print_adj_matrix(self):
        for i in range(self.V):
            for j in range(self.V):
                if j in self.adj[i]:
                    print(1, end=" ")
                else:
                    print(0, end=" ")
            print()

    def bfs(self, s):
        visited = [False] * self.V
        queue = [s]
        visited[s] = True
        while queue:
            s = queue.pop(0)
            print(s, end=" ")
            temp = self.graph[s]
            while temp:
                if not visited[temp.data]:
                    queue.append(temp.data)
                    visited[temp.data] = True
                temp = temp.next

    def dfs(self, s):
        visited = [False] * self.V
        self._dfs_util(s, visited)

    def _dfs_util(self, s, visited):
        """print in DFS order"""
        visited[s] = True
        temp = self.graph[s]
        while temp:
            if not visited[temp.data]:
                self._dfs_util(temp.data, visited)
            temp = temp.next
        print(s, end=" ")

    def topological_sort(self):
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if not visited[i]:
                self._topological_sort_util(i, visited, stack)
        return stack

    def _topological_sort_util(self, s, visited, stack):
        visited[s] = True
        temp = self.graph[s]
        while temp:
            if not visited[temp.data]:
                self._topological_sort_util(temp.data, visited, stack)
            temp = temp.next
        stack.append(s)

    def is_cyclic(self):
        visited = [False] * self.V
        recursion_stack = []
        for i in range(self.V):
            if not visited[i]:
                if self._is_cyclic_util(i, visited, recursion_stack):
                    return True
        return False

    def _is_cyclic_util(self, s, visited, recursion_stack):
        visited[s] = True
        recursion_stack.append(s)
        temp = self.graph[s]
        while temp:
            if temp.data in recursion_stack:
                return True
            if not visited[temp.data]:
                if self._is_cyclic_util(temp.data, visited, recursion_stack):
                    return True
            temp = temp.next
        recursion_stack.pop()
        return False

    def is_connected(self):
        visited = [False] * self.V
        for i in range(self.V):
            if not visited[i]:
                self._is_connected_util(i, visited)
        for i in range(self.V):
            if not visited[i]:
                return False
        return True

    def _is_connected_util(self, s, visited):
        visited[s] = True
        temp = self.graph[s]
        while temp:
            if not visited[temp.data]:
                self._is_connected_util(temp.data, visited)
            temp = temp.next

    def is_path_exists(self, s, d):
        visited = [False] * self.V
        return self._is_path_exists_util(s, d, visited)

    def _is_path_exists_util(self, s, d, visited):
        visited[s] = True
        temp = self.graph[s]
        while temp:
            if temp.data == d:
                return True
            if not visited[temp.data]:
                if self._is_path_exists_util(temp.data, d, visited):
                    return True
            temp = temp.next
        return False

    def is_dag(self):
        return self.is_connected() and not self.is_cyclic()

    def dijkstra(self, s):
        visited = [False] * self.V
        dist = [float("inf")] * self.V
        dist[s] = 0
        pq = []
        heapq.heappush(pq, (0, s))
        while pq:
            u = heapq.heappop(pq)[1]
            if visited[u]:
                continue
            visited[u] = True
            temp = self.graph[u]
            while temp:
                if not visited[temp.data]:
                    if dist[temp.data] > dist[u] + temp.weight:
                        dist[temp.data] = dist[u] + temp.weight
                        heapq.heappush(pq, (dist[temp.data], temp.data))
                temp = temp.next
        # print the distances from source to all other vertices
        print("Vertex\t Distance from vertex {}".format(s))
        for i in range(self.V):
            print("{}\t\t->\t\t{}".format(i, dist[i]))

        return dist

    def bellman_ford(self, s):
        visited = [False] * self.V
        dist = [float("inf")] * self.V
        dist[s] = 0
        for i in range(self.V - 1):
            for u in range(self.V):
                if not visited[u]:
                    temp = self.graph[u]
                    while temp:
                        if dist[temp.data] > dist[u] + temp.weight:
                            dist[temp.data] = dist[u] + temp.weight
                        temp = temp.next
            visited = [False] * self.V
        for u in range(self.V):
            temp = self.graph[u]
            while temp:
                if dist[temp.data] > dist[u] + temp.weight:
                    return False
                temp = temp.next
        return True

    def floyd_warshall(self):
        dist = [[float("inf")] * self.V for i in range(self.V)]
        for i in range(self.V):
            dist[i][i] = 0
            temp = self.graph[i]
            while temp:
                dist[i][temp.data] = temp.weight
                temp = temp.next
        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        return dist

    def shortest_path(self, s, d):
        dist = self.floyd_warshall()
        return dist[s][d]

    def is_bipartite(self):
        visited = [False] * self.V
        color = [None] * self.V
        for i in range(self.V):
            if not visited[i]:
                if not self._is_bipartite_util(i, visited, color):
                    return False
        return True

    def _is_bipartite_util(self, s, visited, color):
        visited[s] = True
        color[s] = True
        temp = self.graph[s]
        while temp:
            if not visited[temp.data]:
                if color[temp.data] == color[s]:
                    return False
                if not self._is_bipartite_util(temp.data, visited, color):
                    return False
            temp = temp.next
        return True

    def is_isomorphic(self, g):
        if self.V != g.V:
            return False
        visited1 = [False] * self.V
        visited2 = [False] * g.V
        for i in range(self.V):
            if not visited1[i]:
                if not self._is_isomorphic_util(i, visited1, visited2, g):
                    return False
        return True

    def _is_isomorphic_util(self, s, visited1, visited2, g):
        visited1[s] = True
        temp = self.graph[s]
        while temp:
            if not visited2[temp.data]:
                if not self._is_isomorphic_util(temp.data, visited1, visited2,
                                                g):
                    return False
            else:
                if g.graph[temp.data].data != temp.data:
                    return False
            temp = temp.next
        return True
