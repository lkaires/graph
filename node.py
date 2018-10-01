#!/usr/bin/python

class Node:

    def __init__(self, name):
        self.indegree = 0
        self.outdegree = 0
        self.inEdges = {}
        self.outEdges = {}
        self.name = name

    def addTo(self, name, value):
        self.outdegree = self.outdegree + 1
        self.outEdges[name] = value

    def addFrom(self, name, value):
        self.indegree = self.indegree + 1
        self.inEdges[name] = value

    def rmTo(self, name):
        self.outdegree = self.outdegree - 1
        del self.outEdges[name]

    def rmFrom(self, name):
        self.indegree = self.indegree - 1
        del self.inEdges[name]

    # Grau do vértice
    # Retorna a quatidade de arestas de entrada ou saída do vértice
    def degree(self):
        return self.indegree + self.outdegree
