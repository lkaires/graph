#!/usr/bin/python

from node import Node
import random

class Graph:

    # Construtor
    def __init__(self) :
        self.nodes = {}

    # Adiciona vértice
    # Recebe nome do vértice
    def addNode(self, name):
        self.nodes[name] = Node(name)

    # Remove vértice
    # Recebe nome do vértice
    def removeNode(self, name):
        for node in self.nodes[name].inEdges:
            self.nodes[node].rmTo(name)
        for node in self.nodes[name].outEdges:
            self.nodes[node].rmFrom(name)
        del self.nodes[name]

    # Conecta dois vértices
    # Recebe os nomes dos vértices a serem conectados
    # Primeiro vértice conecta com o segundo nessa direção
    # Peso da aresta vira 1
    def connect(self, name1, name2):
        if self.nodes.has_key(name1) and self.nodes.has_key(name2):
            self.nodes[name1].addTo(name2, 1)
            self.nodes[name2].addFrom(name1, 1)

    # Conecta dois vértices
    # Recebe os nomes dos vértices a serem conectados e peso da aresta
    # Primeiro vértice conecta com o segundo nessa direção
    def connect(self, name1, name2, value):
        if self.nodes.has_key(name1) and self.nodes.has_key(name2):
            self.nodes[name1].addTo(name2, value)
            self.nodes[name2].addFrom(name1, value)

    # Desconecta dois vértices
    # Recebe os nomes dos vértices a serem desconectados
    def disconnect(self, name1, name2):
        if self.nodes.has_key(name1) and self.nodes.has_key(name2):
            self.nodes[name1].rmTo(name2)
            self.nodes[name2].rmFrom(name1)

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
        return random.choice(self.nodes)

    # Adjacentes
    # Recebe nome do vértice
    # Retorna os vértices ligados ao recebido
    def adjency(self, name):

    # Grau
    # Recebe nome do vértice
    # Retorna número de vértices ligados ao recebido
    def degree(self, name):
        return self.nodes[name].degree()

    # Regular
    # Verifica se todos os vértices possuem o mesmo grau
    # Retorna boolean da verificação
    def regular(self):
        degree = self.randomNode().degree()
        for n in self.nodes:
            if self.nodes[n].degree() != degree:
                return False;
        return True

    # Completo
    # Verifica se todos os vértices se conectam com todos os vértices
    # Retorna boolean da verificação
    def complete(self):
        degree = len(self.nodes)
        for node in self.nodes:
            if self.nodes[node].degree() != degree:
                return False
        return True

    # Fecho Transitivo
    # Recebe nome do vértice
    # Retorna todos os vértices alcançáveis pelo recebido
    def closure(self, name):
        return self.closure(name, {})

    # Fecho Transitivo
    # Recebe o nome do vértice e os vértices já descobertos do fecho transitivo
    # Calcula o fecho transitivo de forma recursiva
    def closure(self, name, closure):
        closure[name] = self.nodes[name]
        for node in closure[name].outEdges:
            if closure.has_key(node) == False:
                self.closure(node, closure)
        return closure

    # Conexo
    # Verifica se existe pelo menos um caminho entre cada par de vértices
    # Retorna boolean da verificação
    def connected(self):
        return self.nodes == self.closure(self.randomNode())

    # Árvore
    # Verifica se não há ciclos no grafo
    # Retorna boolean da verificação
    def tree(self):
        if connected() == False:
            return False

    # Ciclos
    # Verifica se há ciclos
    # Retorna boolean da verificação
    # Calcula o resultado de forma recursiva
    def cycles(self, name1, name2, closure):
        if closure.has_key(name1):
            return True
        closure[name1] = self.nodes[name1]
        for node in self.adjency(name1):
            if node != name2:
                if cycles(node, name1, closure):
                    return True
        del closure[name1]
        return False
