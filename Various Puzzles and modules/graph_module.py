# -*- coding: utf-8 -*-


class node:
    
    def __init__(self, name):
        self.name = name
        self.edges = []
        self.checked = 0
        self.out = []
        
    def add_edge(self, edge_new):
        self.edges.append(edge_new)
        self.out.append(edge_new.get_other())
        
    def remove_edge(self, edge_old):
        self.edges.remove(edge_old)
        self.out.remove(edge_old.nodes.get_other(self))
        
    def connected(self):
        return self.out
        
    def __str__(self):
        return "Node " + str(self.name)
        

class edge:
    
    def __init__(self, node1, node2, d):
        self.a = node1
        self.b = node2
        self.distance = d
    
    def get_other(self):
        return self.b
    


class graph:
    
    def __init__(self, d_dic):
        
        self.nodes = []
        self.trans_d = {}
        
        for node_name in d_dic:
            new_n = node(node_name)
            self.nodes.append(new_n)
            self.trans_d[node_name] = new_n
        
        for node1 in self.nodes:
            
            for node2_name in d_dic[node1.name]:
                node2 = self.trans_d[node2_name]
                connection = edge(node1, node2, d_dic[node1.name][node2.name])
                node1.add_edge(connection)
            

        
    
    
if __name__ == "__main__":
        
    d = {}
    d[1] = {}
    d[2] = {}
    d[3] = {}
    d[4] = {}
    
    d[1][2] = 2
    d[1][3] = 3
    d[2][3] = 1
    d[3][4] = 4
    
    g = graph(d)
        
    
    
    
    
    
    
    
    
    
    
    
    
    

