import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import heap
from my_queue import MyQueue
from custom_thread import CustomThread
import collections


class Graph:
    '''
    Representation for undericted graph 
    '''

    def __init__(self, edges_file_location, columns, is_weighted=True, seperator=" ") -> None:
        df = None
        self.is_weighted = is_weighted
        self.G = None  # Graph by NetworkX
        self.graph_rep = {}  # List representation for running bfs, dijkstras algorithm

        node1 = columns["node1"]
        node2 = columns["node2"]
        weight = columns["weight"]

        if self.is_weighted:
            df = pd.read_csv(edges_file_location,
                             sep=seperator, names=columns.values(), header=None)
            self.G = nx.from_pandas_edgelist(df, node1, node2, [weight])
        else:
            df = pd.read_csv(edges_file_location,
                             sep=seperator, names=columns.values(), header=None)

            self.G = nx.from_pandas_edgelist(df, node1, node2)

        for _, row in df.iterrows():
            if row[node1] not in self.graph_rep:
                self.graph_rep[row[node1]] = []
            if row[node2] not in self.graph_rep:
                self.graph_rep[row[node2]] = []
            if self.is_weighted:
                self.graph_rep[row[node1]].append([row[node2], row[weight]])
                self.graph_rep[row[node2]].append([row[node1], row[weight]])
            else:
                self.graph_rep[row[node1]].append([row[node2]])
                self.graph_rep[row[node2]].append([row[node1]])

    def visualize(self):
        '''
        Creates a visualization of the given graph
        '''
        nx.draw(self.G)
        plt.show()

    def total_nodes_edges(self):
        '''
        Returns the total number of edges and nodes in the graph
        '''
        total_edges = self.G.number_of_edges()
        total_nodes = self.G.number_of_nodes()
        return total_nodes, total_edges

    def average_degree(self):
        '''
        Returns the average number of degree in the graph
        '''
        return np.average([node_deg[1] for node_deg in list(self.G.degree())])

    def density(self):
        '''
        Returns the density of the graph
        '''
        density = 0
        total_nodes, total_edges = self.total_nodes_edges()
        if np.abs(total_nodes) > 1:
            density = 2 * total_edges / (total_nodes * (total_nodes - 1))
        return {"computed": density, "library": nx.density(self.G)}

    def is_connected(self):
        '''
        Checks if the graph is connected
        '''
        return nx.is_connected(self.G)

    def create_priority_queue(self, data):
        '''
        Helper method for creating a Min-Heap from given data
        '''
        data = list(data.items())
        heap.build_max_heap(data)
        return dict(data)

    def get_smallest(self, data):
        '''
        Removes and returns the root element of the given Min-Heap
        '''
        data = list(data.items())
        smallest = heap.pop(data)
        return smallest, dict(data)

    def neighbours(self, vertex):
        '''
        Returns the neighbours of the given vertex
        '''
        return self.graph_rep[vertex]

    def dijkstras(self, start_vertex):
        '''
        Returns the shortest distance from given vertex to all the other vertices
        '''
        # shortest_distances represents the shortest distance travelled to reach a veretex from start_vertex
        shortest_distances = {}

        vertices = self.graph_rep.keys()
        vert_distances = {
            vertex: float('inf') for vertex in vertices if vertex != start_vertex}

        vert_distances[start_vertex] = 0
        vert_distances = self.create_priority_queue(vert_distances)

        while vert_distances:
            smallest, vert_distances = self.get_smallest(vert_distances)
            neighbours_ = self.neighbours(smallest[0])
            for neighbour in neighbours_:
                if neighbour[0] in vert_distances:
                    if smallest[1] + neighbour[1] <= vert_distances[neighbour[0]]:
                        vert_distances[neighbour[0]
                                       ] = smallest[1] + neighbour[1]
                        shortest_distances[neighbour[0]] = (
                            vert_distances[neighbour[0]])
                        vert_distances = self.create_priority_queue(
                            vert_distances)

        return shortest_distances.values()

    def bfs(self, start_vertex):
        '''
        Breadth First Search
        Returns the shortest number of hops required to reach all the vertices from the given vertex  
        '''
        # shortest_paths represents the number of edges hopped to reach a vertex from start_vertex
        shortest_paths = {
            start_vertex: 0
        }
        q = MyQueue()
        q.enqueue(start_vertex)
        visited = [start_vertex]
        while not q.is_empty():
            vertex = q.front()
            neighbours_ = self.neighbours(vertex)
            unmarked = [neighbour[0]
                        for neighbour in neighbours_ if neighbour[0] not in visited]
            if len(unmarked) > 0:
                visited.append(unmarked[0])
                q.enqueue(unmarked[0])
                shortest_paths[unmarked[0]] = shortest_paths[vertex] + 1
            else:
                q.dequeue()
        return shortest_paths.values()

    def eccentricity(self, vertex):
        '''
        Returns the eccentricity of the given vertex
        '''
        shortest_paths = []
        shortest_distances = []
        if self.is_weighted:
            # Use Dijkstra's Algorithm if the graph is weighted
            shortest_distances = self.dijkstras(vertex)
            return max(shortest_distances)
        else:
            # Use BFS Algorithm if the graph is unweighted
            shortest_paths = self.bfs(vertex)
            return max(shortest_paths)

    def diameter(self, big_graph=False):
        '''
        Returns the diameter of the graph
        '''
        eccentricites = []
        vertices = self.graph_rep.keys()
        if self.is_connected():
            if big_graph:
                return nx.diameter(self.G)
            for vertex in vertices:
                # Calculate eccentricity for each vertex
                eccentricites.append(self.eccentricity(vertex))
            return {"computed": max(eccentricites), "library": nx.diameter(self.G)}
        else:
            return ("Cannot compute diameter for disjoint graph")

    def compute_ei(self, vertices):
        '''
        Returns the number of connection between the given set of vertices
        '''
        count = 0

        for vertex in vertices:
            neighbours = [vertex[0] for vertex in self.neighbours(vertex)]
            for neighbour in neighbours:
                if self.is_weighted and neighbour in vertices:
                    # Edge is a list of [vertex, weight]
                    count += 1
                # Edge is a list of [vertex]
                elif not self.is_weighted and neighbour in vertices:
                    count += 1
        return count / 2  # For undirected graph, same edge occurs twice

    def clustering_coefficient(self):
        '''
        Returns the clustering coefficient of the graph
        '''
        clustering_coeffs = []
        for node in self.G.nodes():
            neighbours = [vertex[0] for vertex in self.neighbours(node)]
            ki = len(neighbours)

            ei = self.compute_ei(neighbours)

            if ki > 1:
                ci = (2 * ei) / (ki * (ki - 1))
            else:
                ci = 0

            clustering_coeffs.append(ci)
        return {"computed": sum(clustering_coeffs) / len(clustering_coeffs), "library": nx.average_clustering(self.G)}

    def plot_degree_dist(self):
        nodes_degrees = self.G.degree()
        degree_count = {node_degree[1]: 0 for node_degree in nodes_degrees}
        for node_degree in nodes_degrees:
            degree_count[node_degree[1]] += 1
        total_nodes = len(self.G.nodes())

        for degree in degree_count.keys():
            degree_count[degree] /= total_nodes

        sorted(degree_count.items())

        x = degree_count.keys()
        y = degree_count.values()

        plt.scatter(x, y)
        plt.title("Degree Distribution")
        plt.xlabel("Degree(k)")
        plt.ylabel("P(k)")
        plt.show()
        # degrees_dist = [self.G.degree(n) / total_nodes for n in self.G.nodes()]
        # plt.hist(degrees)
        # plt.show()


graph = Graph("../networks/geo1k_14k/geo1k_14k.mtx",
              {"node1": "A", "node2": "B", "weight": "W", "year": "Year"}, is_weighted=True)


graph.plot_degree_dist()
# graph.visualize()
# print(f" Total nodes and edges: {graph.total_nodes_edges()}")
# print(f" Average Degree: {graph.average_degree()}")
# print(f" Density: {graph.density()}")
# print(f" With Weight, Diameter: {graph.diameter()}")
# graph.is_weighted = False
# print(f" Without Weight, Diameter: {graph.diameter()}")
# print(f" Clustering Coefficient: {graph.clustering_coefficient()}")
