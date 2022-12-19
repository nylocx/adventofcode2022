#  --- Day 16: Proboscidea Volcanium ---
# %% Initialization
import re

import networkx as nx

# %% Read input
G = nx.DiGraph()
nodes_with_flow = {}
with open("day_16_input.txt") as data:
    matches = [re.findall(r"([A-Z]{2}|\d+)", x) for x in data]
for from_, flow, *to in matches:
    G.add_edges_from([(from_, t) for t in to])
    if (f := int(flow)) > 0:
        nodes_with_flow[from_] = f

shortest_path_lengths = dict(nx.all_pairs_shortest_path_length(G))

state_flags = {x: 1 << i for i, x in enumerate(nodes_with_flow)}


def traverse(v, budget, state, flow, answer):
    answer[state] = max(answer.get(state, 0), flow)
    for u, u_flow in nodes_with_flow.items():
        new_budget = budget - shortest_path_lengths[v][u] - 1
        if state_flags[u] & state or new_budget <= 0:
            continue
        traverse(
            u, new_budget, state | state_flags[u], flow + new_budget * u_flow, answer
        )
    return answer


# %% Part 1
max(traverse("AA", 30, 0, 0, {}).values())

# %% Part 2
visited2 = traverse("AA", 26, 0, 0, {})
max(
    v1 + v2 for k1, v1 in visited2.items() for k2, v2 in visited2.items() if not k1 & k2
)
