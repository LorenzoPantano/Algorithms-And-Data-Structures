from list.DoubleLinkedList import ListaDoppiamenteCollegata as List
from abc import ABC, abstractmethod
from dict.trees.treeArrayList import TALNode as TreeNode
from dict.trees.treeArrayList import TreeArrayList as Tree
from datastruct.Queue import CodaArrayList_deque as Queue
from datastruct.Stack import PilaArrayList as Stack
from priorityQueque.PQ_DHeap import PQ_DHeap
from priorityQueque.PQ_BinomialHeap import PQbinomialHeap
from priorityQueque import HeapRilassato


# Modifiche per aggiungere i pesi ai vertici di un grafo
# Sono inclusi in questo file, i file originali Graph.py e Graph_AdjacencyList.py
# Dalla riga 339 parte il file Graph_AdjacencyList.py con relative modifiche
# Le modifiche per i pesi sono evidenziate con un commento #PESO


class Node:
    """
    The graph basic element: node.
    """

    def __init__(self, id, value, weight):     # PESO
        """
        Constructor.
        :param id: node ID (integer).
        :param value: node value.
        """
        self.id = id
        self.value = value
        self.weight = weight       # Viene aggiunto un attributo peso per ogni vertice

    def __eq__(self, other):
        """
        Equality operator.
        :param other: the other node.
        :return: True if ids are equal; False, otherwise.
        """
        return self.id == other.id

    def __str__(self):                  # PESO
        """
        Returns the string representation of the node.
        :return: the string representation of the node.
        """
        return "[{}:{}:{}]".format(self.id, self.value, self.weight)

    def eqWeight(self, other):                          # PESO
        """
        Verifica se due vertici hanno lo stesso peso.
        :param other: altro vertice.
        :return: True se hanno lo stesso peso.
        """
        return self.weight == other.weight


class Edge:
    """
    The graph basic element: (weighted) edge.
    """

    def __init__(self, tail, head, weight=None):
        """
        Constructor.
        :param tail: the tail node ID (integer).
        :param head: the head node ID (integer).
        :param weight: the (optional) edge weight (floating-point).
        """
        self.head = head
        self.tail = tail
        self.weight = weight

    def __cmp__(self, other):
        """
        Compare two edges with respect to their weight.
        :param other: the other edge to compare.
        :return: 1 if the weight is greater than the other;
        -1 if the weight is less than the other; 0, otherwise.
        """
        if self.weight > other.weight:
            return 1
        elif self.weight < other.weight:
            return -1
        else:
            return 0

    def __lt__(self, other):
        """
        Less than operator.
        :param other: the other edge.
        :return: True, if the weight is less than the others; False, otherwise.
        """
        return self.weight < other.weight

    def __gt__(self, other):
        """
        Greater than operator.
        :param other: the other edge.
        :return: True, if the weight is greater than the others; False, otherwise.
        """
        return self.weight > other.weight

    def __eq__(self, other):
        """
        Equality operator.
        :param other: the other edge.
        :return: True if weights are equal; False, otherwise.
        """
        return self.weight == other.weight

    def __str__(self):
        """
        Returns the string representation of the edge.
        :return: the string representation of the edge.
        """
        return "({},{},{})".format(self.tail, self.head, self.weight)


class GraphBase(ABC):
    """
    The basic graph data structure (abstract class).
    """

    def __init__(self):
        """
        Constructor.
        """
        self.nodes = {}  # dictionary {nodeId: node}
        self.nextId = 0  # the next node ID to be assigned

    def isEmpty(self):
        """
        Check if the graph is empty.
        :return: True, if the graph is empty; False, otherwise.
        """
        return not any(self.nodes)

    def numNodes(self):
        """
        Return the number of nodes.
        :return: the number of nodes.
        """
        return len(self.nodes)

    @abstractmethod
    def numEdges(self):
        """
        Return the number of edges.
        :return: the number of edges.
        """
        ...

    @abstractmethod
    def addNode(self, elem, weight):       # PESO
        """
        Add a new node with the specified value.
        :param elem: the node value.
        :param weight: peso del vertice.
        :return: the create node.
        """
        newNode = Node(self.nextId, elem, weight)
        self.nextId += 1
        return newNode

    @abstractmethod
    def deleteNode(self, nodeId):
        """
        Remove the specified node.
        :param nodeId: the node ID (integer).
        :return: void.
        """
        ...

    @abstractmethod
    def getNode(self, id):
        """
        Return the node, if exists.
        :param id: the node ID (integer).
        :return: the node, if exists; None, otherwise.
        """
        ...

    @abstractmethod
    def getNodes(self):
        """
        Return the list of nodes.
        :return: the list of nodes.
        """
        ...

    @abstractmethod
    def insertEdge(self, tail, head, weight=None):
        """
        Add a new edge.
        :param tail: the tail node ID (integer).
        :param head: the head node ID (integer).
        :param weight: the (optional) edge weight (floating-point).
        :return: the created edge, if created; None, otherwise.
        """
        ...

    @abstractmethod
    def deleteEdge(self, tail, head):
        """
        Remove the specified edge.
        :param tail: the tail node ID (integer).
        :param head: the head node ID (integer).
        :return: void.
        """
        ...

    def getEdge(self, tail, head):
        """
        Return the node, if exists.
        :param tail: the tail node ID (integer).
        :param head: the head node ID (integer).
        :return: the edge, if exists; None, otherwise.
        """
        ...

    def getEdges(self):
        """
        Return the list of edges.
        :return: the list of edges.
        """
        ...

    @abstractmethod
    def isAdj(self, tail, head):
        """
        Checks if two nodes ar adjacent.
        :param tail: the tail node ID (integer).
        :param head: the head node ID (integer).
        :return: True, if the two nodes are adjacent; False, otherwise.
        """
        # Note: this method only checks if tail and head exist
        ...


    @abstractmethod
    def getAdj(self, nodeId):
        """
        Return all nodes adjacent to the one specified.
        :param nodeId: the node id.
        :return: the list of nodes adjacent to the one specified.
        :rtype: list
        """
        ...

    @abstractmethod
    def deg(self, nodeId):
        """
        Return the node degree.
        :param nodeId: the node id.
        :return: the node degree.
        """
        ...

    def genericSearch(self, rootId):
        """
        Execute a generic search in the graph starting from the specified node.
        :param rootId: the root node ID (integer).
        :return: the generic exploration tree.
        """
        if rootId not in self.nodes:
            return None

        treeNode = TreeNode(rootId)
        tree = Tree(treeNode)
        vertexSet = {treeNode}  # nodes to explore
        markedNodes = {rootId}  # nodes already explored

        while len(vertexSet) > 0:  # while there are nodes to explore ...
            treeNode = vertexSet.pop()  # get an unexplored node
            adjacentNodes = self.getAdj(treeNode.info)
            for nodeIndex in adjacentNodes:
                if nodeIndex not in markedNodes:  # if not explored ...
                    newTreeNode = TreeNode(nodeIndex)
                    newTreeNode.father = treeNode
                    treeNode.sons.append(newTreeNode)
                    vertexSet.add(newTreeNode)
                    markedNodes.add(nodeIndex)  # mark as explored
        return tree

    def bfs(self, rootId):
        """
        Execute a Breadth-First Search (BFS) in the graph starting from the
        specified node.
        :param rootId: the root node ID (integer).
        :return: the BFS list of nodes.
        """
        # if the root does not exists, return None
        if rootId not in self.nodes:
            return None

        # BFS nodes initialization
        bfs_nodes = []

        # queue initialization
        q = Queue()
        q.enqueue(rootId)

        explored = {rootId}  # nodes already explored

        while not q.isEmpty():  # while there are nodes to explore ...
            node = q.dequeue()  # get the node from the queue
            explored.add(node)  # mark the node as explored
            # add all adjacent unexplored nodes to the queue
            for adj_node in self.getAdj(node):
                if adj_node not in explored:
                    q.enqueue(adj_node)
            bfs_nodes.append(node)

        return bfs_nodes

    def dfs(self, rootId):
        """
        Execute a Depth-First Search (DFS) in the graph starting from the
        specified node.
        :param rootId: the root node ID (integer).
        :return: the DFS list of nodes.
        """
        # if the root does not exists, return None
        if rootId not in self.nodes:
            return None

        # DFS nodes initialization
        dfs_nodes = []

        # queue initialization
        s = Stack()
        s.push(rootId)

        explored = {rootId}  # nodes already explored

        while not s.isEmpty():  # while there are nodes to explore ...
            node = s.pop()  # get the node from the stack
            explored.add(node)  # mark the node as explored
            # add all adjacent unexplored nodes to the stack
            for adj_node in self.getAdj(node):
                if adj_node not in explored:
                    s.push(adj_node)
            dfs_nodes.append(node)

        return dfs_nodes

    @abstractmethod
    def print(self):
        """
        Print the graph.
        :return: void.
        """
        ...


class GraphAdjacencyList(GraphBase):
    """
    A graph, implemented as an adjacency list.
    Each node u has a list containing its adjacent nodes, that is nodes v such
    that exists an edges (u,v).
    Let's define deg(v) = degree of vertex v, or t
    ---
    Memory Complexity: O(|V|+|E|)
    """

    def __init__(self):
        """
        Constructor.
        """
        super().__init__()
        self.adj = {}  # adjacency lists {nodeID:listOfAdjacentNodes}

    def numEdges(self):
        """
        Return the number of edges.
        :return: the number of edges.
        """
        return sum(len(adj_list) for adj_list in self.adj.values())

    def addNode(self, elem, weight):     # PESO
        """
        Add a new node with the specified value.
        :param elem: the node value.
        :param weight: peso del vertice.
        :return: the create node.
        """
        newnode = super().addNode(elem, weight)  # create a new node with the correct ID

        self.nodes[newnode.id] = newnode  # add the new node to the dictionary
        self.adj[newnode.id] = List()  # create the adjacency list for the new node

        return newnode

    def deleteNode(self, nodeId):
        """
        Remove the specified node.
        O(m)
        :param nodeId: the node ID (integer).
        :return: void.
        """
        try:
            self.nodes[nodeId]  # check if nodeId exists
        except KeyError:
            return   # node with nodeId not present

        # remove the node from the set of nodes, that is to remove the node
        # from the dictionary nodes
        del self.nodes[nodeId]

        # remove all edges starting from the node, that is to remove the
        # adjacency list for the node
        del self.adj[nodeId]

        # remove all edges pointing to the node, that is to remove the node
        # from all the adjacency lists
        for adj in self.adj.values():
            curr = adj.getFirstRecord()
            while curr is not None:
                if curr.elem == nodeId:
                    adj.deleteRecord(curr)
                curr = curr.next

    def deg(self, nodeId):
        """
        Return the node degree.
        :param nodeId: the node id.
        :return: the node degree.
        """
        if nodeId not in self.nodes:
            return 0
        else:
            return len(self.adj[nodeId])

    def getNode(self, id):
        """
        Return the node, if exists.
        :param id: the node ID (integer).
        :return: the node, if exists; None, otherwise.
        """
        return None if id not in self.nodes else self.nodes[id]

    def getNodes(self):
        """
        Return the list of nodes.
        :return: the list of nodes.
        """
        return list(self.nodes.values())

    def insertEdge(self, tail, head, weight=None):
        """
        Add a new edge.
        :param tail: the tail node ID (integer).
        :param head: the head node ID (integer).
        :param weight: the (optional) edge weight (floating-point).
        :return: the created edge, if created; None, otherwise.
        """
        # if tail and head exist, add the entry into the adjacency list
        if tail in self.nodes and head in self.nodes:  # TODO overwrite if edge already exists
            self.adj[tail].addAsLast(head)

    def deleteEdge(self, tail, head):
        """
        Remove the specified edge.
        :param tail: the tail node ID (integer).
        :param head: the head node ID (integer).
        :return: void.
        """
        # if tail and head exist, delete the edge
        if tail in self.nodes and head in self.nodes:
            curr = self.adj[tail].getFirstRecord()
            while curr is not None:
                if curr.elem == head:
                    self.adj[tail].deleteRecord(curr)
                    break
                curr = curr.next

    def getEdge(self, tail, head):
        """
        Return the node, if exists.
        :param tail: the tail node ID (integer).
        :param head: the head node ID (integer).
        :return: the edge, if exists; None, otherwise.
        """
        if tail in self.nodes and head in self.nodes:
            curr = self.adj[tail].getFirstRecord()
            while curr is not None:
                if curr.elem == head:
                    return Edge(tail, head, None)
                curr = curr.next
        return None

    def getEdges(self):
        """
        Return the list of edges.
        :return: the list of edges.
        """
        edges = []
        for adj_item in self.adj.items():
            curr = adj_item[1].getFirstRecord()
            while curr is not None:
                edges.append(Edge(adj_item[0], curr.elem, None))
                curr = curr.next
        return edges

    def isAdj(self, tail, head):
        """
        Checks if two nodes ar adjacent.
        :param tail: the tail node ID (integer).
        :param head: the head node ID (integer).
        :return: True, if the two nodes are adjacent; False, otherwise.
        """
        if tail == head:        # Aggiunto confronto per cui ogni nodo e' adiacente con se stesso.
            return True         # Utile nella generazione di un grafo casuale

        # if tail and head exist, look for the entry in the adjacency list
        if tail in self.nodes and head in self.nodes:
            curr = self.adj[tail].getFirstRecord()
            while curr is not None:
                nodeId = curr.elem
                if nodeId == head:
                    return True
                curr = curr.next

        # else, return False
        return False

    def getAdj(self, nodeId):
        """
        Return all nodes adjacent to the one specified.
        :param nodeId: the node id.
        :return: the list of nodes adjacent to the one specified.
        """
        result = []
        curr = self.adj[nodeId].getFirstRecord()
        while curr is not None:
            result.append(curr.elem)
            curr = curr.next
        return result

    def print(self):
        """
        Print the graph.
        :return: void.
        """
        # if the adjacency list is empty ...
        if self.isEmpty():
            print("Adjacency List: EMPTY")
            return

        # else ...
        print("Adjacency Lists:")
        for adj_item in self.adj.items():
            print("{}:{}".format(adj_item[0], adj_item[1]))

    def maxWeightNode(self):       # PESO
        """
        Ritorna il vertice con peso maggiore.
        :return: vertice con peso maggiore.
        """
        if self.isEmpty():
            print("Graph is empty")
            return None
        else:
            maxNode = self.nodes[0]
            for node in self.nodes.values():
                if node.weight > maxNode.weight:
                    maxNode = node
            print(f"Max node is: ID {maxNode.id} Value {maxNode.value} Weight {maxNode.weight}") # Per stampare
            return maxNode

    def modifyWeightNode(self, nodeId, newWeight):    # PESO
        """
        Modifica il peso di un vertice con il nuovo peso
        :param nodeId: vertice da modificare.
        :param newWeight: nuovo peso da mettere nel vertice.
        :return: None
        """
        if len(self.nodes) == 0:
            print("Graph is empty")
            return None
        else:
            for node in self.nodes.values():
                if node.id == nodeId:
                    node.weight = newWeight
                    return

    def printNodes(self):   # PESO
        """
        Permette di stampare tutti i vertici del grafo con i loro pesi
        :return: None
        """
        if len(self.nodes) == 0:
            print("Graph is empty")
            return None
        else:
            for node in self.nodes.values():
                print(f"Node ID: {node.id}  Value: {node.value}  Weight: {node.weight}")
        return None

    def visitaInPrioritaDHeap(self, d):        # VISITA IN PRIORITA'
        """
        Visita di un grafo, basata su quella generica, dove l'insieme F e' una coda con
        priorita e il vertice con peso maggiore e' quello a priorita maggiore.
        Versione con DHeap come coda con priorita'.
        :return: Lista che contiene i nodi visitati in ordine, il primo e' quello a priorità' magggiore.
        """
        node = self.maxWeightNode()
        node.weight = - node.weight   # La coda con priorita' PQ_DHeap e' basata sul minimo, invertendo il valore dei
        if node.id not in self.nodes:    # pesi quello che era il massimo peso diventa il minimo...
            return None

        result = []
        result.append(node) # Lista risulato della visita, nodi visitati in ordine
        vertexSet = PQ_DHeap(d) # Insieme F (Coda con priorita')
        vertexSet.insert(node.id, node.weight)
        node.weight = - node.weight
        markedNodes = [node.id]
        while not vertexSet.isEmpty():  # while there are nodes to explore ...
            node = vertexSet.deleteMin()
            adjNodes = self.getAdj(node.elem)
            for nodeIndex in adjNodes:
                if nodeIndex not in markedNodes:
                    node1 = self.getNode(nodeIndex)
                    node1.weight = - node1.weight
                    vertexSet.insert(nodeIndex, node1.weight)
                    node1.weight = - node1.weight
                    markedNodes.append(nodeIndex)
                    result.append(node1)
        # Print the results
        # for elem in result:
            # print(f"Node ID: {elem.id}  Value: {elem.value}  Weight: {elem.weight}")
        return result

    def visitaInPrioritaBinomialHeap(self):        # VISITA IN PRIORITA'
        """
        Visita di un grafo, basata su quella generica, dove l'insieme F e' una coda con
        priorita e il vertice con peso maggiore e' quello a priorita maggiore.
        Versione con Heap Binomiale come coda con priorita'.
        :return: Lista che contiene i nodi visitati in ordine, il primo e' quello a priorità' magggiore.
        """
        node = self.maxWeightNode()
        node.weight = - node.weight   # La coda con priorita' PQ_DHeap e' basata sul minimo, invertendo il valore dei
        if node.id not in self.nodes:    # pesi quello che era il massimo peso diventa il minimo...
            return None

        result = []
        result.append(node) # Lista risulato della visita, nodi visitati in ordine
        vertexSet = PQbinomialHeap() # Insieme F (Coda con priorita')
        vertexSet.insert(node.id, node.weight)
        node.weight = - node.weight
        markedNodes = [node.id]
        while not vertexSet.isEmpty():  # while there are nodes to explore ...
            node = vertexSet.findMin()
            vertexSet.deleteMin()
            adjNodes = self.getAdj(node)
            for nodeIndex in adjNodes:
                if nodeIndex not in markedNodes:
                    node1 = self.getNode(nodeIndex)
                    node1.weight = - node1.weight
                    vertexSet.insert(nodeIndex, node1.weight)
                    node1.weight = - node1.weight
                    markedNodes.append(nodeIndex)
                    result.append(node1)
        # Print the results
        # for elem in result:
            # print(f"Node ID: {elem.id}  Value: {elem.value}  Weight: {elem.weight}")
        return result

    def visitaInPrioritaHeapBinomialeRilassato(self):     # VISITA IN PRIORITA'
        """
        Visita di un grafo, basata su quella generica, dove l'insieme F e' una coda con
        priorita e il vertice con peso maggiore e' quello a priorita maggiore.
        Versione con Heap Binomiale come coda con priorita'.
        :return: Lista che contiene i nodi visitati in ordine, il primo e' quello a priorità' magggiore.
        """
        node = self.maxWeightNode()
        if node.id not in self.nodes:
            return None

        result = []
        result.append(node) # Lista risulato della visita, nodi visitati in ordine
        vertexSet = HeapRilassato.PQbinomialHeapRelaxed() # Insieme F (Coda con priorita')
        vertexSet.insert(node.id, node.weight)
        markedNodes = [node.id]
        while not vertexSet.isEmpty():  # while there are nodes to explore ...
            node = vertexSet.findMax()
            vertexSet.deleteMax()
            adjNodes = self.getAdj(node.elem)
            for nodeIndex in adjNodes:
                if nodeIndex not in markedNodes:
                    node1 = self.getNode(nodeIndex)
                    vertexSet.insert(nodeIndex, node1.weight)
                    markedNodes.append(nodeIndex)
                    result.append(node1)
        #Print the results
        #for elem in result:
            #print(f"Node ID: {elem.id}  Value: {elem.value}  Weight: {elem.weight}")
        return result

