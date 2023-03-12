import networkx as nx
network = nx.Graph()
network.add_nodes_from([1,2,3])
print(f"This network has now {network.number_of_nodes()} nodes.")

network.add_edge(6,7)
network.add_edge(6,5)
network.add_edge(7,3)
network.add_edge(5,3)
network.add_edge(3,1)
network.add_edge(4,1)
network.add_edge(2,1)
network.add_edge(2,4)
network.add_edge(5,1)


import matplotlib.pyplot as plt
color_list = ["gold", "red", "violet","green","violet","red","yellow"]
plt.figure(figsize=(8, 6))
plt.title('Example of Graph Representation', size=10)

nx.draw_networkx(network,node_color=color_list, with_labels=True)

plt.show()
