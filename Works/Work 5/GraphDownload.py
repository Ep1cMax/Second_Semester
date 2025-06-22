import osmnx as ox

G = ox.graph_from_place('Сараево, Босния', network_type='drive')
ox.save_graphml(G, 'Saraevo_roads.graphml')