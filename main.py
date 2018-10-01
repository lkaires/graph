#!/usr/bin/python

from graph import Graph

def main():
    graph = Graph()

    # Matérias da primeira fase
    graph.addNode("INE5401")
    graph.addNode("INE5402")
    graph.addNode("INE5403")
    graph.addNode("EEL5105")
    graph.addNode("MTM3100")
    graph.addNode("MTM3101")

    # Dependência da primeira fase
    graph.connect("MTM3100", "MTM3101")

    # Matérias da segunda fase
    graph.addNode("INE5404")
    graph.addNode("INE5405")
    graph.addNode("INE5406")
    graph.addNode("INE5407")
    graph.addNode("MTM3102")
    graph.addNode("MTM5512")

    # Dependências da segunda fases
    graph.connect("MTM3101", "MTM3102")
    graph.connect("MTM3101", "INE5405")
    graph.connect("INE5402", "INE5404")
    graph.connect("EEL5105", "INE5406")

    # Matérias da terceira fase
    graph.addNode("INE5408")
    graph.addNode("INE5410")
    graph.addNode("INE5409")
    graph.addNode("MTM5245")
    graph.addNode("INE5411")

    # Dependências da terceira fase
    graph.connect("INE5404", "INE5408")
    graph.connect("INE5404", "INE5410")
    graph.connect("MTM3102", "INE5409")
    graph.connect("MTM5512", "INE5409")
    graph.connect("MTM5512", "MTM5245")
    graph.connect("INE5406", "INE5411")

    # Matérias da quarta fase
    graph.addNode("INE5417")
    graph.addNode("INE5413")
    graph.addNode("INE5415")
    graph.addNode("INE5416")
    graph.addNode("INE5412")
    graph.addNode("INE5414")

    # Dependências da quarta fase
    graph.connect("INE5408", "INE5417")
    graph.connect("INE5408", "INE5413")
    graph.connect("INE5403", "INE5413")
    graph.connect("INE5408", "INE5415")
    graph.connect("INE5403", "INE5415")
    graph.connect("INE5408", "INE5416")
    graph.connect("INE5411", "INE5412")
    graph.connect("INE5410", "INE5412")
    graph.connect("INE5404", "INE5414")

    # Matérias da quinta fase
    graph.addNode("INE5419")
    graph.addNode("INE5423")
    graph.addNode("INE5420")
    graph.addNode("INE5421")
    graph.addNode("INE5418")
    graph.addNode("INE5422")

    # Dependências da quinta fase
    graph.connect("INE5417", "INE5419")
    graph.connect("INE5408", "INE5423")
    graph.connect("MTM3102", "INE5420")
    graph.connect("MTM5245", "INE5420")
    graph.connect("INE5415", "INE5421")
    graph.connect("INE5412", "INE5418")
    graph.connect("INE5414", "INE5418")
    graph.connect("INE5414", "INE5422")

    # Matérias da sexta fase
    graph.addNode("INE5427")
    graph.addNode("INE5453")
    graph.addNode("INE5425")
    graph.addNode("INE5430")
    graph.addNode("INE5426")
    graph.addNode("INE5424")

    # Dependências da sexta fase
    graph.connect("INE5419", "INE5427")
    graph.connect("INE5419", "INE5453")
    graph.connect("INE5405", "INE5425")
    graph.connect("INE5405", "INE5430")
    graph.connect("INE5416", "INE5430")
    graph.connect("INE5421", "INE5426")
    graph.connect("INE5412", "INE5424")

    # Matérias da sétima fase
    graph.addNode("INE5433")
    graph.addNode("INE5432")
    graph.addNode("INE5429")
    graph.addNode("INE5431")
    graph.addNode("INE5428")

    # Dependências da sétima fase
    graph.connect("INE5427", "INE5433")
    graph.connect("INE5453", "INE5433")
    graph.connect("INE5423", "INE5432")
    graph.connect("INE5403", "INE5429")
    graph.connect("INE5415", "INE5429")
    graph.connect("INE5414", "INE5429")
    graph.connect("INE5414", "INE5431")
    graph.connect("INE5407", "INE5428")

    # Matérias da oitava fase
    graph.addNode("INE5434")

    # Dependências da oitava fase
    graph.connect("INE5433", "INE5434")

    # Ordenação topológica
    print("Ordenação topológica:")
    for node in graph.topologic():
        print(node)

if __name__ == "__main__" :
    main()
