# nwx
import networkx as nx

# our files
from zigbee import *
from thread import *

# define LAN
LAN = nx.Graph()

# add main router
LAN.add_node("lan_router", latency=random.uniform(0.1, 10))

LAN = thread_setup(LAN)
LAN = zigbee_setup(LAN)

plot_graph(LAN)