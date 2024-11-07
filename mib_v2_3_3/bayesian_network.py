from mib_v2_3_3.distrib import Distrib
class nodo:
    def __init__(self, distrib: Distrib, level:int, parents:set = None, children:set = None):
        self.distrib = distrib
        self.level = level
        self.parents = parents
        self.children = children

   
class network:
    def __init__(self, nodos:set):
        
        self.nodos = list(nodos)
        self.nodos.sort(key=lambda x: x.level)

    
        