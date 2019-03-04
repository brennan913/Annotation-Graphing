import sys
#import matplotlib
import matplotlib.pyplot as plt
#import plotly.plotly as ply
#import plotly.graph_objs as go
import networkx as nx
import networkx.drawing


from ann_to_graph import generate_edges
def main(argc, argv):
    test3()

def test2():
    plt.ioff()
    G = nx.petersen_graph()
    nx.draw(G, with_labels=True, font_weight='bold')
    #print(plt.subplot(122))
    nx.draw_shell(G, nlist=[range(5,10), range(5)], with_labels=True, font_weight='bold')
    plt.show()

def test3():
    plt.ioff()
    dod= {'start': {'finish':{'weight':1}}} # single edge (0,1)
    G=nx.from_dict_of_dicts(dod)
    nx.draw(G, with_labels=True, font_weight='bold', node_color='beige')
    plt.show()

def test1(argc, argv):
    if argc != 2:
        sys.stderr.write('usage: {} <filename>\n'.format(argv[0]))
        return 1

    edges = generate_edges(argv[1])
    print()
    print(edges)
    print()

    nx.draw(G, with_labels=True, font_weight='bold')
    #print(plt.subplot(122))
    nx.draw_shell(G, nlist=[range(5,10), range(5)], with_labels=True, font_weight='bold')
    plt.show()



if __name__=="__main__":
    main(len(sys.argv), sys.argv)