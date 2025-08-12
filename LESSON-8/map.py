import networkx as nx
import matplotlib.pyplot as plt

# Create graph
G = nx.Graph()

# Add nodes with attributes
G.add_node("SWIFT", size=100, color="#1f77b4")
G.add_node("VTB", size=40, color="#d62728")
G.add_node("SPFS", size=70, color="#ff7f0e")
G.add_node("CIPS", size=70, color="#2ca02c")
G.add_node("India", size=60, color="#9467bd")
G.add_node("Rupee-Ruble", size=50, color="#17becf")

# Add edges
G.add_edge("VTB", "SWIFT", style="dashed", color="#7f7f7f", weight=1)
G.add_edge("VTB", "SPFS", style="solid", color="#ff7f0e", weight=4)
G.add_edge("VTB", "CIPS", style="solid", color="#2ca02c", weight=4)
G.add_edge("VTB", "Rupee-Ruble", style="solid", color="#17becf", weight=4)
G.add_edge("India", "Rupee-Ruble", style="solid", color="#9467bd", weight=3)

# Draw graph
pos = nx.spring_layout(G, seed=42)  # Positions
colors = nx.get_node_attributes(G, 'color').values()
sizes = [G.nodes[n]['size']*20 for n in G.nodes]

nx.draw_networkx_nodes(G, pos, node_color=colors, node_size=sizes)
nx.draw_networkx_labels(G, pos)

# Draw edges with styles
for u,v,attr in G.edges(data=True):
    nx.draw_networkx_edges(G, pos, edgelist=[(u,v)], 
                           style=attr['style'], 
                           width=attr['weight'], 
                           edge_color=attr['color'])

plt.title("SWIFT Disconnection: Global Financial Fragmentation (2022-2023)")
plt.axis("off")
plt.show()