import networkx as nx
from matplotlib import pyplot as plt

# create graph
T = nx.Graph()

# define thread device types

# add 2 border routers
T.add_node("thread_BR0", type="border")
T.add_node("thread_BR1", type="border")

# add thread leader
T.add_node("thread_L0")

# create six thread mesh devices
for i in range(6):
    T.add_node(f"thread_R{i}")

# mesh 'em
for i in range(6):
    for j in range(6):
        if(i!=j):
            T.add_edge(f"thread_R{i}", f"thread_R{j}")

print(T.edges)

nx.draw(T, with_labels=True)
plt.show()
