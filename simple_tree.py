import networkx as nx
import matplotlib.pyplot as plt

graph = nx.full_rary_tree(3, 26)

# Define node positions
pos = nx.spring_layout(graph, center=None) 
# pos = nx.circular_layout(graph)
# pos = nx.random_layout(graph)
# pos = nx.shell_layout(graph)
# pos = nx.spectral_layout(graph)

print(pos)

# Draw the tree
nx.draw(graph, pos=pos, with_labels=False, node_size=120, node_color="black", font_size=8, font_weight="bold")
plt.title("Simple Tree")
# plt.show()
plt.savefig('simple_tree.png')
plt.savefig('simple_tree.pdf')


