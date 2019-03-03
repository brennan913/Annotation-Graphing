import sys
import re
from arg_graph import *

def main(argc, argv):
    if argc != 2:
        sys.stderr.write('usage: {} <filename>\n'.format(argv[0]))
        return 1

    nodes = {}
    edges = {}
    filename = argv[1]
    annotation_file = open(filename, 'r')
    for line in annotation_file:
        line = line.rstrip('\n')

        #sys.stdout.write(str(line.split('\t')) + '\n')

        # pattern one: r'T\d
        # example input:
        # 'T3      Premise 11 54   Olympic events are rooted in old traditions'
        # TODO make_arg_node(str) -> arg_node
        if line[0] == 'T':
            line = line.split('\t') # ['T3', 'Premise 11 54', 'Olympic events are rooted in old traditions']
            adu_id = line[0] # 'T3'
            label = Label(line[1].split()[0]) # 'Premise'
            adu = line[2] # 'Olympic events are rooted in old traditions'
            
            nodes[adu_id] = arg_node(adu_id, adu, label)

        # pattern two: r'R\d
        # example input:
        # 'R1      supports Arg1:T3 Arg2:T2'
        # TODO make_relation_edge(str) -> relation_edge
        elif line[0] == 'R':
            line = line.split('\t') # ['R1', 'supports Arg1:T3 Arg2:T2']
            relation_id = line[0] # 'R1'
            relation_details = line[1].split() # ['supports', 'Arg1:T3', 'Arg2:T2']
            relation = Relation(relation_details[0]) # 'supports
            start = re.sub(r'(Arg)\d+:', '', relation_details[1]) # 'T3'
            end = re.sub(r'(Arg)\d+:', '', relation_details[2]) # 'T2'

            edges[relation_id] = relation_edge(nodes[start], nodes[end], relation)

        # pattern three: r'A\d
        # example input:
        # 'A2      Stance T2 For'
        elif line[0] == 'A':
            line = line.split('\t') # ['A2', 'Stance T2 For']
            stance_details = line[1].split() # ['Stance', 'T2', 'For']
            adu_id = stance_details[1] # 'T2'
            stance = Stance(stance_details[2]) # 'For'

            nodes[adu_id].stance= stance 

            
    #print(nodes)
    #print('\n\n\n\n')
    print(edges)
    
    annotation_file.close()


if __name__ == "__main__":
    main(len(sys.argv), sys.argv)