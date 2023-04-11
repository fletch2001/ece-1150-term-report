import random
import networkx as nx

def route(network, source, dest):
    # if dest not in network.nodes:
        # add routing delay?

    path = nx.shortest_path(network, source, dest, "latency")
    path_latency = sum([network[path[i]][path[i+1]]["latency"] for i in range(len(path)-1)])

    return path_latency

def dissimilar_random_ints(lower, upper, count):
    return_list = []
    for n in range(count):
        i = random.randint(lower, upper)
        while i in return_list:
            i = random.randint(lower, upper)
        return_list.append(i)

    return return_list