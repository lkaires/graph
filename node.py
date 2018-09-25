#!/usr/bin/python

class Node:

    def __init__(self, name):
        self.degree = 0
        self.mark = False
        self.name = name

    def addEdge(self):
        degree++

    def rmEdge(self):
        degree--

    # Marca o nodo
    # Recebe boolean
    # Atualiza mark para o valor passado
    def mark(self, mark):
        self.mark = mark
