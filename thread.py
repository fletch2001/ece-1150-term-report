import random

import networkx as nx
import networkx.classes
from matplotlib import pyplot as plt

def thread_setup(scale, lan_network):
    # set network size parameters first
    thread_num_nodes = scale * 6

    # create graph
    T = nx.Graph()

    # define thread device types

    # create six thread mesh devices
    for i in range(thread_num_nodes):
        T.add_node(f"thread_R{i}")

    # mesh 'em
    for i in range(thread_num_nodes):
        for j in range(thread_num_nodes):
            if i != j:
                # connect all non-same nodes and add latency to edge
                T.add_edge(f"thread_R{i}", f"thread_R{j}", latency=random.uniform(0.01, 0.1))

    # add a random number of edge nodes to each mesh node
    for i in range(thread_num_nodes):
        for n in range(random.randint(1, 10)):
            T.add_node(f"thread_dev_{i}_{n}")
            # add latency again
            T.add_edge(f"thread_R{i}", f"thread_dev_{i}_{n}", latency=random.uniform(0.01, 0.1))

    # randomly choose leader
    leader_index = random.randint(0, thread_num_nodes - 1)
    T.nodes[f"thread_R{leader_index}"]["leader"] = True

    # determine number of border routers
    num_borders = random.randint(1, scale * 3)

    border_indexes = []

    # designate border routers
    for n in range(num_borders):
        i = random.randint(0, thread_num_nodes - 1)
        while i in border_indexes:
            i = random.randint(0, thread_num_nodes - 1)

        border_indexes.append(i)

    # compose/join networks into one lan network
    lan_network = nx.compose(T, lan_network)

    plot_graph(lan_network)

    # set border routers
    for n in range(num_borders):
        lan_network.nodes[f"thread_R{border_indexes[n]}"]["border"] = True

        # connect border routers to LAN
        lan_network.add_edge("lan_router", f"thread_R{border_indexes[n]}", latency=random.uniform(0.01, 0.1))

    return lan_network

def route(network, source, dest):
    # if dest not in network.nodes:
        # add routing delay?

    path = nx.shortest_path(network, source, dest, "latency")
    path_latency = sum([network[path[i]][path[i+1]]["latency"] for i in range(len(path)-1)])

# time
# hops
# network layout
#

def plot_graph(graph):
    print(graph.edges)

    nx.draw(graph, with_labels=True)
    plt.show()
