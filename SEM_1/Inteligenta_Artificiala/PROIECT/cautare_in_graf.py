import heapq
import sys

import networkx as nx
import matplotlib.pyplot as plt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QInputDialog


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_node(self, node):
        self.nodes.add(node)

    def add_edge(self, from_node, to_node, distance):
        self.edges.setdefault(from_node, []).append((to_node, distance))
        self.edges.setdefault(to_node, []).append(
            (from_node, distance)
        )  # Pentru un graf neorientat

    def dijkstra(self, start_node, end_node):
        distances = {node: float("infinity") for node in self.nodes}
        distances[start_node] = 0
        pq = [(0, start_node)]
        path = {}

        while pq:
            current_distance, current_node = heapq.heappop(pq)

            if current_node == end_node:
                break

            for neighbor, weight in self.edges.get(current_node, []):
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
                    path[neighbor] = current_node

        # Reconstruiește calea cea mai scurtă
        shortest_path = []
        while end_node in path:
            shortest_path.insert(0, end_node)
            end_node = path[end_node]
        shortest_path.insert(0, start_node)

        return shortest_path


class GraphInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.graph = Graph()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Algoritm de cautare in Graf')

        # Layout
        layout = QVBoxLayout()
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)
        centralWidget.setLayout(layout)

        # Add Node
        self.addNodeButton = QPushButton('Adauga Nod', self)
        self.addNodeButton.clicked.connect(self.addNode)
        layout.addWidget(self.addNodeButton)

        # Add Edge
        self.addEdgeButton = QPushButton('Adauga Muchie', self)
        self.addEdgeButton.clicked.connect(self.addEdge)
        layout.addWidget(self.addEdgeButton)

        # Find Path
        self.findPathButton = QPushButton('Gaseste calea cea mai scurta', self)
        self.findPathButton.clicked.connect(self.findPath)
        layout.addWidget(self.findPathButton)

        # Graph Canvas
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        layout.addWidget(self.canvas)

        self.show()

    def addNode(self):
        node, ok = QInputDialog.getText(self, 'Nod', 'Introdu numele nodului:')
        if ok:
            self.graph.add_node(node)
            self.plotGraph()

    def addEdge(self):
        from_node, ok = QInputDialog.getText(self, 'Sursa', 'Introdu punctul de pornire:')
        if ok:
            to_node, ok = QInputDialog.getText(self, 'Destinatie', 'Introdu destinatia:')
            if ok:
                weight, ok = QInputDialog.getInt(self, 'Greutate', 'Introdu greutatea muchiei:')
                if ok:
                    self.graph.add_edge(from_node, to_node, weight)
                    self.plotGraph()

    def findPath(self):
        start_node, ok = QInputDialog.getText(self, 'Sursa', 'Introdu punctul de pornire:')
        if ok:
            end_node, ok = QInputDialog.getText(self, 'Destinatie', 'Introdu destinatia:')
            if ok:
                shortest_path = self.graph.dijkstra(start_node, end_node)
                self.plotGraph(shortest_path)

    def plotGraph(self, shortest_path=None):
        self.figure.clear()
        G = nx.Graph()

        for node in self.graph.nodes:
            G.add_node(node)
        for start, edges in self.graph.edges.items():
            for end, weight in edges:
                G.add_edge(start, end, weight=weight)

        pos = nx.spring_layout(G, seed=42)  # Păstrăm pozițiile constante

        # Definirea culorilor
        node_color = "#DDB5F2"
        edge_color = "#B4E8E0"
        text_color = "#25273A"
        highlight_color = "#990F02"

        nx.draw(G, pos, with_labels=True, node_color=node_color, font_color=text_color, node_size=2000, edge_color=edge_color)
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color=text_color)

        if shortest_path:
            edges_in_path = list(zip(shortest_path, shortest_path[1:]))
            nx.draw_networkx_edges(G, pos, edgelist=edges_in_path, edge_color=highlight_color, width=2)

        self.canvas.draw()

# Rularea aplicației
app = QApplication(sys.argv)
ex = GraphInterface()
sys.exit(app.exec_())
