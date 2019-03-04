import sys
#import matplotlib
import matplotlib.pyplot as plt
#import plotly.plotly as ply
#import plotly.graph_objs as go
import networkx as nx
import networkx.drawing


from ann_to_graph import *

def main(argc, argv):
    test4(argc, argv)
    #test3()

def test4(argc, argv):
    if argc != 2:
        sys.stderr.write('usage: {} <filename>\n'.format(argv[0]))
        return 1
    
    # parse file into graph
    edges = generate_edges(argv[1])
    dod = to_dict_of_dicts(edges)

    plt.ioff()
    G = nx.DiGraph(dod)
    nx.draw(G, with_labels=True, font_weight='bold', font_size=5, node_size=3000, node_color='beige')
    #nx.draw_networkx_edge_labels(G, )
    plt.show()

def test2():
    plt.ioff()
    G = nx.petersen_graph()
    nx.draw(G, with_labels=True, font_weight='bold')
    #print(plt.subplot(122))
    nx.draw_shell(G, nlist=[range(5,10), range(5)], with_labels=True, font_weight='bold')
    plt.show()

def test3():
    plt.ioff()
    dod= {'start': {'almost':{'weight':1}}, 'almost': {'end':{'weight':1000}}} # single edge (0,1)
    #G=nx.from_dict_of_dicts(dod)
    G = nx.DiGraph(dod)
    nx.draw(G, with_labels=True, font_weight='bold', node_color='beige')
    #nx.draw_networkx_edge_labels()
    plt.show()

def test1(argc, argv):
    if argc != 2:
        sys.stderr.write('usage: {} <filename>\n'.format(argv[0]))
        return 1
    
    edges = generate_edges(argv[1])
    print()
    print(edges)
    print()


if __name__=="__main__":
    main(len(sys.argv), sys.argv)