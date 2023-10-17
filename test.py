import copy
from graphviz import Digraph

# Create the original Digraph object
original_digraph = Digraph()
original_digraph.node('A')
original_digraph.node('B')
original_digraph.edge('A', 'B')

# Duplicate the Digraph object
duplicated_digraph = copy.deepcopy(original_digraph)

# Test the duplication
print(original_digraph.source)
print(duplicated_digraph.source)
