# nwx
import networkx as nx

# our files
from zigbee import *
from thread import *

def dissimilar_random_ints(lower, upper, count):
    return_list = []
    for n in range(count):
        i = random.randint(lower, upper)
        while i in return_list:
            i = random.randint(lower, upper)
        return_list.append(i)

    return return_list

# SETUP

# define LAN
LAN = nx.Graph()

# add main router
LAN.add_node("lan_router", latency=random.uniform(0.1, 10))

# LAN = thread_setup(1, LAN)
LAN = zigbee_setup(16, LAN)

plot_graph(LAN)

# RUN

SIM_RUNS = 5
NUM_PACKETS = 100

# get total number of nodes
total_nodes = LAN.number_of_nodes()

for sim_run in range(SIM_RUNS):

    for pkt_num in range(NUM_PACKETS):
        # get source and destination randomly
        source_dest = dissimilar_random_ints(0, total_nodes - 1, 2)
        print(source_dest)

        node_list = list(LAN.nodes)
        source = node_list[source_dest[0]]
        dest = node_list[source_dest[1]]
        print(source, dest)

        route(LAN, source, dest)
