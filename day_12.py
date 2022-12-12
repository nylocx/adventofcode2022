#  --- Day 12: Hill Climbing Algorithm ---
# %% Initialization
import numpy as np
import networkx as nx

# %% Read input
with open("day_12_input.txt") as data:
    heightmap = np.array(
        [[ord(x) - 97 for x in line] for line in data.read().strip().split("\n")]
    )
sy, sx = [x[0] for x in np.where(heightmap == -14)]
ey, ex = [x[0] for x in np.where(heightmap == -28)]
heightmap[sy, sx] = ord("a") - 97
heightmap[ey, ex] = ord("z") - 97

G = nx.grid_2d_graph(*heightmap.shape, create_using=nx.DiGraph)
G.remove_edges_from([e for e in nx.edges(G) if heightmap[e[1]] > heightmap[e[0]] + 1])

# %% Part 1
shortest = len(nx.bidirectional_shortest_path(G, (sy, sx), (ey, ex))) - 1
print("Length of shortest path from S:", shortest)

# %% Part 2
xy, xx = np.where(heightmap == 0)
for sy, sx in zip(xy, xx):
    try:
        s = len(nx.bidirectional_shortest_path(G, (sy, sx), (ey, ex))) - 1
        shortest = s if s < shortest else shortest
    except nx.exception.NetworkXNoPath:
        pass

print("Length of shortest path from elevation zero:", shortest)
