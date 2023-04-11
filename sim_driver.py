# nwx
from time import time

import networkx as nx
import os

# our files
from helpers import *

from zigbee import *
from thread import *

# SETUP

latencies = []
num_nodes = []

runs_per_size = 5

start_time = time()

for s in range(1, 9):
    current_size_latencies = []
    current_size_num_nodes = []

    # define LAN
    LAN = nx.Graph()
    # add main router
    LAN.add_node("lan_router", latency=0.01)
    LAN, thread_nodes = thread_setup(s, LAN)
    LAN, zigbee_nodes = zigbee_setup(s, LAN)

    total_nodes = thread_nodes + zigbee_nodes
    total_nodes_with_router = total_nodes + 1

    # current_size_num_nodes.append(total_nodes)
    for t in range(runs_per_size):


        # RUN

        SIM_RUNS = 5
        NUM_PACKETS = 100

        # to hold latency experienced by packet 0-99
        latency = []

        for pkt_num in range(NUM_PACKETS):
            # get source and destination randomly
            source_dest = dissimilar_random_ints(0, total_nodes - 1, 2)

            node_list = list(LAN.nodes)
            source = node_list[source_dest[0]]
            dest = node_list[source_dest[1]]

            # add latency to latency array
            latency.append(route(LAN, source, dest))

        current_size_latencies.append(sum(latency) / NUM_PACKETS)

        # save network to image
        nx.draw(LAN, with_labels=True)

        save_plt_to_png(f"simoutput/networks/lan{t}_{total_nodes}_nodes.png")

    latencies.append(sum(current_size_latencies) / runs_per_size)
    num_nodes.append(total_nodes)

total_time = time() - start_time
print(f"simulation finished in {total_time} sec.")

# make figure
fig, ax = plt.subplots()
ax.plot(num_nodes, latencies)
ax.set_title("effect of LAN network size (in nodes) on relative latency")
ax.set_xlabel("average number of nodes")
ax.set_ylabel("average latency per packet")


save_plt_to_png('simoutput/simplot.png')
plt.show()
