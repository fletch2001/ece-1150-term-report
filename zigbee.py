import random

import networkx as nx
import matplotlib.pyplot as plt


def zigbee_setup(lan_network):
    G = nx.Graph()
    # create arrays to store routers and end devices
    routers = []
    eds = []

    # create mesh topology routers
    G.add_node('R1')
    routers.append('R1')
    G.add_node('R2')
    routers.append('R2')

    # create end devices
    for i in range(8):
        G.add_node('ED' + str(i))
        eds.append('ED' + str(i))

    # add edges from router to router
    G.add_edge('R1', 'R2')

    # add edges from router to router
    G.add_edge('R1', 'R2', latency=random.uniform(0.01, 0.1))

    # add edges from router to end devices
    for i in range(4):
        G.add_edge('R1', 'ED' + str(i), latency=random.uniform(0.01, 0.1))

    for i in range(4):
        G.add_edge('R2', 'ED' + str(i+4), latency=random.uniform(0.01, 0.1))

    lan_network.add_edge("lan_router", "R1", latency=random.uniform(0.1, 1))
