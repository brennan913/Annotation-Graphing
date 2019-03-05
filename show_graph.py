import sys
import matplotlib.pyplot as plt
import networkx as nx
import networkx.drawing

from ann_to_graph import *

def main(argc, argv):
    show_graph(argc, argv)

def show_graph(argc, argv):
    if argc != 2:
        sys.stderr.write('usage: {} <filename>\n'.format(argv[0]))
        return 1
    
    # parse file into graph
    edges = generate_edges(argv[1])
    dod = to_dict_of_dicts(edges)

    plt.ioff()
    G = nx.DiGraph(dod)
    pos = nx.spring_layout(G)
    nx.draw(G, pos=pos, with_labels=True, font_weight='bold', font_size=5, node_size=2500, node_color='beige', labels={n:n for n in G.nodes()})
    
    labels = {}
    for edge in edges:
        labels[(edge.start, edge.end)]=edge.relation.name

    nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=labels, font_size=10, font_color='xkcd:blue gray')
    plt.axis('on')
    plt.show()
    

if __name__=="__main__":
    main(len(sys.argv), sys.argv)