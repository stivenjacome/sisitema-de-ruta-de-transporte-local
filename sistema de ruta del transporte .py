import networkx as nx
import matplotlib.pyplot as plt

# Definir el grafo del sistema de transporte
G = nx.Graph()

# Agregar estaciones y conexiones
G.add_nodes_from(["A", "B", "C", "D", "E"])
G.add_edges_from([("A", "B"), ("B", "C"), ("B", "D"), ("C", "E"), ("D", "E")])

# Visualizar el grafo
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=8, font_color="black", font_weight="bold", edge_color="gray")
plt.show()

# Encontrar la ruta más corta
start = "A"
end = "E"
shortest_path = nx.shortest_path(G, source=start, target=end)

print(f"La ruta más corta desde {start} hasta {end}: {shortest_path}")



