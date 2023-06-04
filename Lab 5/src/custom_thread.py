import time
from threading import Thread


class CustomThread(Thread):

    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, Verbose=None) -> None:
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None

    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)

    def join(self):
        Thread.join(self)
        return self._return


def add(n1, n2):
    time.sleep(5)
    return n1+n2


# Test code

# sums = [(1, 2), (2, 3), (4, 5), (6, 7), (7, 8), (8, 9), (10, 12)]

# threads = [CustomThread(target=add, args=(summm)) for summm in sums]

# results = []

# for thread in threads:
#     thread.start()
#     # results.append(thread.join())

# for thread in threads:
#     results.append(thread.join())


# print(results)

# import networkx as nx
# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy as np
# import heap
# from my_queue import MyQueue
# import threading


# class Graph:

#     def __init__(self, edges_file_location, columns, is_weighted=True) -> None:
#         df = None
#         self.is_weighted = is_weighted
#         self.G = None
#         self.graph_rep = {}

#         node1 = columns["node1"]
#         node2 = columns["node2"]
#         weight = columns["weight"]

#         if self.is_weighted:
#             df = pd.read_csv(edges_file_location,
#                              sep=" ", names=columns.values(), header=None)
#             self.G = nx.from_pandas_edgelist(df, node1, node2, [weight])
#         else:
#             df = pd.read_csv(edges_file_location,
#                              sep=" ", names=columns.values(), header=None)

#             self.G = nx.from_pandas_edgelist(df, node1, node2)
#         for _, row in df.iterrows():
#             if row[node1] not in self.graph_rep:
#                 self.graph_rep[row[node1]] = []
#             if row[node2] not in self.graph_rep:
#                 self.graph_rep[row[node2]] = []
#             if self.is_weighted:
#                 self.graph_rep[row[node1]].append([row[node2], row[weight]])
#                 self.graph_rep[row[node2]].append([row[node1], row[weight]])
#             else:
#                 self.graph_rep[row[node1]].append([row[node2]])
#                 self.graph_rep[row[node2]].append([row[node1]])

#     def visualize(self):
#         nx.draw(self.G)
#         plt.show()

#     def total_nodes_edges(self):
#         total_edges = self.G.number_of_edges()
#         total_nodes = self.G.number_of_nodes()
#         return total_nodes, total_edges

#     def average_degree(self):
#         return np.average([node_deg[1] for node_deg in list(self.G.degree())])

#     def density(self):
#         total_nodes, total_edges = self.total_nodes_edges()
#         if np.abs(total_nodes) > 1:
#             return 2 * total_edges / (total_nodes * (total_nodes - 1))
#         else:
#             return 0

#     def is_connected(self):
#         return nx.is_connected(self.G)

#     def create_priority_queue(self, data):
#         data = list(data.items())
#         heap.build_max_heap(data)
#         return dict(data)

#     def get_smallest(self, data):
#         data = list(data.items())
#         smallest = heap.pop(data)
#         return smallest, dict(data)

#     def neighbours(self, vertex):
#         return self.graph_rep[vertex]

#     def dijkstras(self, start_vertex):
#         # shortest_distances represents the shortest distance travelled to reach a veretex from start_vertex
#         shortest_distances = {}

#         vertices = self.graph_rep.keys()
#         vert_distances = {
#             vertex: float('inf') for vertex in vertices if vertex != start_vertex}

#         vert_distances[start_vertex] = 0
#         vert_distances = self.create_priority_queue(vert_distances)

#         while vert_distances:
#             smallest, vert_distances = self.get_smallest(vert_distances)
#             neighbours_ = self.neighbours(smallest[0])
#             for neighbour in neighbours_:
#                 if neighbour[0] in vert_distances:
#                     if smallest[1] + neighbour[1] <= vert_distances[neighbour[0]]:
#                         vert_distances[neighbour[0]
#                                        ] = smallest[1] + neighbour[1]
#                         shortest_distances[neighbour[0]] = (
#                             vert_distances[neighbour[0]])
#                         vert_distances = self.create_priority_queue(
#                             vert_distances)

#         return shortest_distances.values()

#     def bfs(self, start_vertex):
#         # shortest_paths represents the number of edges hopped to reach a vertex from start_vertex
#         shortest_paths = {
#             start_vertex: 0
#         }
#         q = MyQueue()
#         q.enqueue(start_vertex)
#         visited = [start_vertex]
#         while not q.is_empty():
#             vertex = q.front()
#             neighbours_ = self.neighbours(vertex)
#             unmarked = [neighbour[0]
#                         for neighbour in neighbours_ if neighbour[0] not in visited]
#             if len(unmarked) > 0:
#                 visited.append(unmarked[0])
#                 q.enqueue(unmarked[0])
#                 shortest_paths[unmarked[0]] = shortest_paths[vertex] + 1
#             else:
#                 q.dequeue()
#         return shortest_paths.values()

#     def eccentricity(self, vertex):
#         shortest_paths = []
#         shortest_distances = []
#         if self.is_weighted:
#             shortest_distances = self.dijkstras(vertex)
#             return max(shortest_distances)
#         else:
#             shortest_paths = self.bfs(vertex)
#             return max(shortest_paths)

#     def diameter(self):
#         eccentricites = []
#         vertices = self.graph_rep.keys()
#         if self.is_connected():
#             for vertex in vertices:
#                 eccentricites.append(self.eccentricity(vertex))
#             return {"computed": max(eccentricites), "library": nx.diameter(self.G)}
#         else:
#             return ("Cannot compute diameter for disjoint graph")

#     def custering_coefficient(self):
#         # return (nx.average_clustering(self.G))
#         clusters = []
#         for node in self.G.nodes():
#             neighbors = [neighbor for neighbor in self.G.neighbors(node)]
#             ki = len(neighbors)
#             subgraph = nx.subgraph(self.G, neighbors)
#             ei = subgraph.number_of_edges()
#             if ki != 0 and ki != 1:
#                 ci = (2 * ei) / (ki * (ki - 1))
#             else:
#                 ci = 0
#             clusters.append(ci)
#         clusteringCoeff = sum(clusters) / len(clusters)
#         return clusteringCoeff


# graph = Graph("../networks/lasftm_asia/lastfm_asia_edges.csv",
#               {"node1": "A", "node2": "B", "weight": "W", "year": "Year"}, is_weighted=False)
# # print(graph.custering_coefficient())
# print(graph.diameter())
