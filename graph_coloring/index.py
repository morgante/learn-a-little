'''
https://www.interviewcake.com/question/python/graph-coloring
'''

import random

class GraphNode:
    
    def __init__(self, label):
        self.label = label
        self.neighbors = set()
        self.color = None

def color_graph(graph, colors):
    for node in graph:
        if not node.color:
            bad_colors = [n.color for n in node.neighbors if n.color]
            for color in colors:
                if color not in bad_colors:
                    node.color = color

def print_graph(graph):
    for node in graph:
        string = "{label}: {color} - {colors}".format(
            label=node.label,
            color=node.color,
            colors=[n.color for n in node.neighbors]
        )
        print(string)

a = GraphNode('a')
b = GraphNode('b')
c = GraphNode('c')

a.neighbors.add(b)
b.neighbors.add(a)
b.neighbors.add(c)
b.neighbors.add(b)
c.neighbors.add(b)

graph = [a, b, c]

color_graph(graph, ['red', 'blue', 'green'])
print_graph(graph)
