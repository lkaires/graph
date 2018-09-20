#!/usr/bin/python

class Graph:

    nodes = {}
    edges = {}

    # Adiciona vértice
    # Recebe nome do vértice
    def addNode(self, name):
        nodes[name] = Node()
        edges[name] = set([])

    # Remove vértice
    # Recebe nome do vértice
    def removeNode(self, name):
        for n in edges[name]:
            edges[n].discard(name)
        del edges[name]
        del nodes[name]

    # Conecta dois vértices
    # Recebe os nomes dos vértices a serem conectados
    def connect(self, name1, name2):
        if nodes.has_key(name1) and nodes.has_key(name2):
            edges[name1].add(name2)
            edges[name2].add(name1)

    # Desconecta dois vértices
    # Recebe os nomes dos vértices a serem desconectados
    def disconnect(self, name1, name2):
        if nodes.has_key(name1) and nodes.has_key(name2):
            edges[name1].discard(name2)
            edges[name2].discard(name1)

    # Ordem do grafo
    # Retorna o número de vértices do grafo
    def order(self):
        return len(nodes)

    # Vértices
    # Retorna os vértices do grafo
    def nodes(self):
        return nodes;

    # Vértice
    # Retorna um vértice aleatório do grafo
    def randomNode(self):

    # Adjacentes
    # Recebe nome do vértice
    # Retorna os vértices ligados ao recebido
    def adjency(self, name):
        return edges[name]

    # Grau
    # Recebe nome do vértice
    # Retorna número de vértices ligados ao recebido
    def degree(self, name):
        return nodes[name].degree

    # Regular
    # Verifica se todos os vértices possuem o mesmo grau
    # Retorna boolean da verificação
    def regular(self):
        degree = randomNome().degree
        for n in node:
            temp = n.degree
            if temp != degree:
                return False;
            degree = temp
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
