import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()


# create mesh topology routers
G.add_node('R1')
G.add_node('R2')

# create end devices
for i in range(8):
    G.add_node('ED' + str(i))

# add edges from router to router
G.add_edge('R1', 'R2')

# add edges from router to end devices
for i in range(4):
    G.add_edge('R1', 'ED' + str(i))

for i in range(4):
    G.add_edge('R2', 'ED' + str(i+4))

# plot network
nx.draw(G, with_labels=True)
plt.show()