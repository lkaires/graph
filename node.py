#!/usr/bin/python

class Node:

    def __init__(self, name):
        self.indegree = 0
        self.outdegree = 0
        self.inEdges = {}
        self.outEdges = {}
        self.mark = False
        self.name = name

    def addTo(self, name, value):
        self.outdegree++
        self.outEdges[name] = value

    def addFrom(self, name, value):
        self.indegree++
        self.inEdges[name] = value

    def rmTo(self, name):
        self.outdegree--
        del self.outEdges[name]

    def rmFrom(self, name):
        self.indegree--
        del self.inEdges[name]

    # Grau do vértice
    # Retorna a quatidade de arestas de entrada ou saída do vértice
    def degree(self):
        return self.indegree + self.outdegree

    # Marca o nodo
    # Recebe boolean
    # Atualiza mark para o valor passado
    def mark(self, mark):
        self.mark = mark
