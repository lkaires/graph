#!/usr/bin/python

class Node:

    def __init__(self, name):
        self.indegree = 0
        self.outdegree = 0
        self.inEdge = {}
        self.outEdge = {}
        self.mark = False
        self.name = name

    def addTo(self):
        self.outdegree++

    def addFrom(self):
        self.indegree++

    def rmTo(self):
        self.outdegree--

    def rmFrom(self):
        self.indegree--

    # Marca o nodo
    # Recebe boolean
    # Atualiza mark para o valor passado
    def mark(self, mark):
        self.mark = mark
