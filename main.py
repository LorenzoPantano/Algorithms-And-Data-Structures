"""
Lorenzo Pantano: 0240471
Andrea Tamburrini: 0240885
Main del progetto: Definisce una funzione per generare un grafo connesso, non orientato e pesato sui vertici;
Le varie versioni dell'algoritmo visitaInPriorita', in particolare con DHeap, Heap Binomiale e Heap Binomiale Rilassato
sono contenute nel file GraphConModifiche.py
"""

import GraphConModifiche
import random

def generaGrafo(nodes):
    """
    Genera un grafo connesso, non orientato e pesato sui vertici, il numero di archi sara' minimo nodes - 1
    dove nodes e' il numero di nodi (che viene passato come parametro) di cui sarà composto il grafo.
    Si fa uso del modulo random, generando pseudo-casualmente sia l'elemento che contiene il vertice
    sia il suo peso: l'ID del vertice viene dato da i (indice di scorrimento del for).
    :param nodes: numero di nodi (vertici).
    :return: grafo rappresentato con liste di adiacenza.
    """
    graph = GraphConModifiche.GraphAdjacencyList()
    for i in range(0, nodes):
        nodeElem = random.randint(0, nodes*10)
        nodeWeigth = random.randint(0, nodes*100)
        graph.addNode(nodeElem, nodeWeigth)
        if i >= 1:                               # Aggiungiamo un arco tra due nodi successivi, in modo che
            graph.insertEdge(i-1, i)             # il grafo risulti sicuramente connesso, poi aggiungiamo altri archi
            graph.insertEdge(i, i-1)             # casualmente che colleghino altri vertici (verificando che non siano
    for i in range(0, nodes):                    # gia' connessi)
        tail = random.randint(0, nodes-1)
        head = random.randint(0, nodes-1)
        if not graph.isAdj(tail, head):
            graph.insertEdge(tail, head)
        if not graph.isAdj(head, tail):
            graph.insertEdge(head, tail)
    return graph

# TEST EFFETTUATI

# 100 NODI
grafo = generaGrafo(100)
grafo.printNodes()
grafo.visitaInPrioritaHeapBinomialeRilassato()
grafo.visitaInPrioritaBinomialHeap()
grafo.visitaInPrioritaDHeap(10)
grafo.visitaInPrioritaDHeap(5)
grafo.visitaInPrioritaDHeap(2)

# 500 NODI
# grafo = generaGrafo(500)
# grafo.visitaInPrioritaHeapBinomialeRilassato()
# grafo.visitaInPrioritaBinomialHeap()
# grafo.visitaInPrioritaDHeap(10)
# grafo.visitaInPrioritaDHeap(5)
# grafo.visitaInPrioritaDHeap(2)

# 1000 NODI
"""
grafo = generaGrafo(1000)
grafo.visitaInPrioritaHeapBinomialeRilassato()
grafo.visitaInPrioritaBinomialHeap()
grafo.visitaInPrioritaDHeap(10)
grafo.visitaInPrioritaDHeap(5)
grafo.visitaInPrioritaDHeap(2)
"""

# 2000 NODI
"""
grafo = generaGrafo(2000)
grafo.visitaInPrioritaHeapBinomialeRilassato()
grafo.visitaInPrioritaBinomialHeap()
grafo.visitaInPrioritaDHeap(10)
grafo.visitaInPrioritaDHeap(5)
grafo.visitaInPrioritaDHeap(2)
"""


# 5000 NODI
"""
grafo = generaGrafo(5000)
grafo.visitaInPrioritaHeapBinomialeRilassato()
grafo.visitaInPrioritaBinomialHeap()
grafo.visitaInPrioritaDHeap(10)
grafo.visitaInPrioritaDHeap(5)
grafo.visitaInPrioritaDHeap(2)
"""
