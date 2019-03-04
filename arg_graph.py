from enum import Enum

class Relation(Enum):
    SUPPORT = 'supports'
    ATTACK = 'attacks'

class Label(Enum):
    MAIN_CLAIM = 'Main Claim' # TODO need to confirm 
    CLAIM = 'Claim'
    PREMISE = 'Premise'

class Stance(Enum):
    FOR = 'For'
    AGAINST = 'Against' # TODO need to confirm
    NONE = None

class arg_node:
    def __init__(self, adu_id, adu, label, stance=Stance(None)):
        self.id = adu_id
        self.adu = adu
        self.label = label
        self.stance = stance

    def __str__(self):
        return '\n\nid:{}\nlabel:{}\nstance:{}\nadu:[{}]'.format(self.id, self.label.name, self.stance.name, self.adu)

    def __repr__(self):
        #return '\n\nid:{}\nlabel:{}\nstance:{}\nadu:[{}]'.format(self.id, self.label.name, self.stance.name, self.adu)
        return self.id

class relation_edge:
    def __init__(self, start, end, relation):
        #self.start = arg_node(start_adu, start_label)
        #self.end = arg_node(end_adu, end_label)
        self.start = start
        self.end = end
        self.relation = relation


    def __str__(self):
        return '{}--{}--{}'.format(self.start.id, self.relation.name, self.end.id)
    
    def __repr__(self):
        return '{}--{}--{}'.format(self.start.id, self.relation.name, self.end.id)

def to_dict_of_dicts(edges):
    dd = {}
    for edge in edges:
        start = edge.start
        end = edge.end
        

        dd[start] = {end:{'weight':1}}


    return dd

