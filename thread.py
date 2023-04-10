import random

import networkx as nx
from matplotlib import pyplot as plt

def thread_setup(lan_router):
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
            if i != j:
                # connect all non-same nodes and add latency to edge
                T.add_edge(f"thread_R{i}", f"thread_R{j}", latency=random.uniform(0.01, 0.1))

    # add a random number of edge nodes to each mesh node
    for i in range(6):
        for n in range(random.randint(1, 8)):
            T.add_node(f"thread_dev_{i}_{n}")
            # add latency again
            T.add_edge(f"thread_R{i}", f"thread_dev_{i}_{n}", latency=random.uniform(0.01, 0.1))

    # randomly choose leader
    leader_index = random.randint(0, 6)
    T.nodes[f"thread_R{leader_index}"]["leader"] = True

    # set border router
    border_index = random.randint(0, 6)
    T.nodes[f"thread_R{border_index}"]["border"] = True

    # connect border router to LAN
    T.add_edge(lan_router, f"thread_R{border_index}", latency=random.uniform(0.01, 0.1))

def route_thread(network, source, dest):
    if dest not in network.nodes:
        # add routing delay?


def plot_graph(Graph):
    print(Graph.edges)

    nx.draw(Graph, with_labels=True)
    plt.show()
