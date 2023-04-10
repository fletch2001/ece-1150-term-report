import networkx as nx
import random
import matplotlib.pyplot as plt

# Set up network topology
G = nx.Graph()

# Add nodes for IoT networks
for i in range(2):
    G.add_node(f"R{i}", type="R")

# Add nodes for LAN routers
for i in range(3):
    G.add_node(f"LAN{i}", type="LAN")

# Add edges between IoT networks and LAN routers
for i in range(3):
    for j in range(3):
        G.add_edge(f"IoT{i}", f"LAN{j}", latency=random.uniform(0.01, 0.1))

# Add edges between LAN routers
for i in range(2):
    G.add_edge(f"LAN{i}", f"LAN{i+1}", latency=random.uniform(0.01, 0.1))

nx.draw(G, with_labels=True)
plt.show()

# Simulate packet transmission
source = "IoT0"
dest = "IoT2"

# Compute the shortest path through LAN routers
lan_path = nx.shortest_path(G, source, dest, weight="latency")
lan_latency = sum([G[lan_path[i]][lan_path[i+1]]["latency"] for i in range(len(lan_path)-1)])

# Compute the shortest path through IoT networks using 6LoWPAN protocol
for i in range(3):
    G.nodes[f"IoT{i}"]["latency"] = 0.01  # set baseline latency for IoT networks
    G.nodes[f"IoT{i}"]["packet_size"] = random.randint(10, 50)  # set random packet size for each node
ioT_path = []

for i in range(len(lan_path)-1):
    edge = (lan_path[i], lan_path[i+1])
    if G.nodes[lan_path[i]]["type"] == "IoT":
        # compress packet using 6LoWPAN before sending over LAN
        packet_size = G.nodes[lan_path[i]]["packet_size"]
        compressed_size = packet_size // 2
        G[lan_path[i]][lan_path[i+1]]["latency"] += 0.001 * compressed_size  # add additional latency for compression
        G.add_edge(f"{lan_path[i]}_6LoWPAN", lan_path[i+1], latency=0.001 * compressed_size)  # add edge for compressed packet
        ioT_path.append(f"{lan_path[i]}_6LoWPAN")
    else:
        ioT_path.append(lan_path[i])

# compute latency for 6LoWPAN path
ioT_path.append(dest)
ioT_latency = sum([G[ioT_path[i]][ioT_path[i+1]]["latency"] for i in range(len(ioT_path)-1)])

# Simulate random number of packets sent over time
time = []
latency = []
num_packets = random.randint(5, 20)

for i in range(num_packets):
    packet_size = random.randint(10, 50)
    G.nodes[source]["packet_size"] = packet_size
    ioT_latency = sum([G[ioT_path[i]][ioT_path[i+1]]["latency"] for i in range(len(ioT_path)-1)])
    time.append(i)
    latency.append(ioT_latency)

# Plot latency over time
plt.plot(time, latency)
plt.xlabel("Time (packets)")
plt.ylabel("Latency (seconds)")
plt.title("Latency over time for random packets sent between IoT networks")
plt.show()
