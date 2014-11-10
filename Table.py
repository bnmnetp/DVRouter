'''
Created on Nov 5, 2014

@author: daviis01
'''
class Table():
    
    def __init__(self):
        self.neighbors = {}
        self.data = {}
        self.routerName = ""
        
    def __str__(self):
        st = 'table'
        for name in self.data:
            st += "\t" + name
        st += "\n\t"
        for name in self.data:
            st += '\t' + str(self.data[name][0])
        return st
    
    def addNeighbor(self, name, cost, ip):
        self.neighbors[name] = ip
        self.data[name] = [cost, name]
        
    def addSelf(self, name):
        self.routerName = name
        self.data[name] = [0, name]
        
    def checkUpdate(self, name, cost, neighName):
        """
        @name:str
        @cost:int
        @nighName:str
        """
        totalCost = cost + self.data[neighName][0]
        if name in self.data:
            if self.data[name][0] > totalCost:
                self.data[name] = [totalCost, neighName]
                return True
            else:
                return False
        else:
            self.data[name] = [totalCost, neighName]
            return True
        
    def toReport(self):
        repDict = {}
        for key in self.data:
            if key != self.routerName:
                repDict[key] = self.data[key][0]
        return repDict
        