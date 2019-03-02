from enum import Enum

class Relation(Enum):
    SUPPORT = 1
    ATTACK = 2

class Label(Enum):
    MAIN_CLAIM = 1
    CLAIM = 2
    PREMISE = 3

class arg_node:
    def __init__(self, adu_id, adu, label):
        self.id = adu_id
        self.adu = adu
        self.label = label

class relation_edge:
    def __init__(self, start_adu, start_label, end_adu, end_label, relation):
        self.start = arg_node(start_adu, start_label)
        self.end = arg_node(end_adu, end_label)
        self.relation = relation

