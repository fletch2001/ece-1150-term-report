import random
import os
import networkx as nx
from matplotlib import pyplot as plt


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


def plot_graph(graph):
    print(graph.edges)

    nx.draw(graph, with_labels=True)
    plt.show()

def save_plt_to_png(file_name):
    current_directory_path = os.getcwd()
    split_file_path = file_name.split('/')
    # make subfolder if there is one and it doesn't exist
    if len(split_file_path) >= 2:
        subfolder_name = '/'.join(split_file_path[0:len(split_file_path) - 1])
        subfolder_path = os.path.join(current_directory_path, subfolder_name)
        if not os.path.exists(subfolder_path):
            os.makedirs(subfolder_path)
        file_name = os.path.join(subfolder_path, split_file_path[len(split_file_path) - 1])
    plt.savefig(file_name)
