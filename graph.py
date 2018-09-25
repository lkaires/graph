#!/usr/bin/python

import Node in node.py
import random

class Graph:

    # Construtor
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    # Adiciona vértice
    # Recebe nome do vértice
    def addNode(self, name):
        self.nodes[name] = Node(name)
        self.edges[name] = set([])

    # Remove vértice
    # Recebe nome do vértice
    def removeNode(self, name):
        for n in self.edges[name]:
            self.edges[n].discard(name)
            self.nodes[n].rmEdge()
        del self.edges[name]
        del self.nodes[name]

    # Conecta dois vértices
    # Recebe os nomes dos vértices a serem conectados
    def connect(self, name1, name2):
        if self.nodes.has_key(name1) and self.nodes.has_key(name2):
            self.edges[name1].add(name2)
            self.nodes[name1].addEdge()
            self.edges[name2].add(name1)
            self.nodes[name2].addEdge()

    # Desconecta dois vértices
    # Recebe os nomes dos vértices a serem desconectados
    def disconnect(self, name1, name2):
        if nodes.has_key(name1) and nodes.has_key(name2):
            self.edges[name1].discard(name2)
            self.nodes[name1].rmEdge()
            self.edges[name2].discard(name1)
            self.nodes[name2].rmEdge()

    # Ordem do grafo
    # Retorna o número de vértices do grafo
    def order(self):
        return len(self.nodes)

    # Vértices
    # Retorna os vértices do grafo
    def nodes(self):
        return self.nodes

    # Vértice
    # Retorna um vértice aleatório do grafo
    def randomNode(self):
        random.choice(self.nodes)

    # Adjacentes
    # Recebe nome do vértice
    # Retorna os vértices ligados ao recebido
    def adjency(self, name):
        return self.edges[name]

    # Grau
    # Recebe nome do vértice
    # Retorna número de vértices ligados ao recebido
    def degree(self, name):
        return self.nodes[name].degree

    # Regular
    # Verifica se todos os vértices possuem o mesmo grau
    # Retorna boolean da verificação
    def regular(self):
        degree = randomNome().degree
        for n in self.nodes:
            temp = n.degree
            if temp != degree:
                return False;
        return True

    # Completo
    # Verifica se todos os vértices se conectam com todos os vértices
    # Retorna boolean da verificação
    def complete(self):

    # Fecho Transitivo
    # Recebe nome do vértice
    # Retorna todos os vértices alcançáveis pelo recebido
    def closure(self, name):

    # Conexo
    # Verifica se existe pelo menos um caminho entre cada par de vértices
    # Retorna boolean da verificação
    def connected(self):

    # Árvore
    # Verifica se não há ciclos no grafo
    # Retorna boolean da verificação
    def tree(self):
