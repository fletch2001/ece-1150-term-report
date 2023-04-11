import random
import math
import networkx as nx


def zigbee_setup(scale, lan_network):
    zigbee_num_nodes = scale * 8
    zigbee_max_devices_per_router = 65

    # zigbee accommodates up to 65 devices per router. Default to 2, but scale up if there are more
    # than 65 devices per router
    zigbee_num_routers = math.ceil(zigbee_num_nodes / zigbee_max_devices_per_router)
    if zigbee_num_routers < 2:
        zigbee_num_routers = 2  # default to 2

    G = nx.Graph()

    # create arrays to store routers and end devices
    routers = []
    eds = []

    # create mesh topology routers
    for r in range(zigbee_num_routers):
        G.add_node(f'z_R{r}')  # add each router to graph
        routers.append(f'z_R{r}')  # add to list as well

    # create end devices
    for i in range(zigbee_num_nodes):
        G.add_node('z_ED' + str(i))
        eds.append('z_ED' + str(i))

    # mesh 'em
    for i in range(zigbee_num_routers):
        for j in range(zigbee_num_routers):
            if i != j:
                # connect all non-same nodes and add latency to edge
                G.add_edge(f"z_R{i}", f"z_R{j}", latency=0.01)

    zigbee_devices_per_router = zigbee_num_nodes / zigbee_num_routers

    devices_assigned = 0
    curr_router = 0

    # assign devices to routers round-robin-ly so each router has a similar number of devices
    while devices_assigned < zigbee_num_nodes:
        G.add_edge(f"z_R{curr_router}", f"z_ED{devices_assigned}", latency=0.01)

        # go to next router
        curr_router = (curr_router + 1) % zigbee_num_routers
        devices_assigned += 1

    total_nodes = len(G.nodes)

    # compose zigbee/G into LAN network
    lan_network = nx.compose(G, lan_network)

    # connect LAN router to zigbee routers
    for r in range(zigbee_num_routers):
        lan_network.add_edge('lan_router', f'z_R{r}', latency=0.01)

    return lan_network, total_nodes
