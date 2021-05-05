from ..list.LinkedList import ListaCollegata
from ..datastruct.Queue import CodaArrayList_deque as queue

class BinomialHeapNode:
    def __init__(self, element, key):
        self.elem = element
        self.key = key
        self.father = None
        self.sons = ListaCollegata()

    def swap(self, otherNode):
        self.elem, otherNode.elem = otherNode.elem, self.elem
        self.key, otherNode.key = otherNode.key, self.key

    def addSon(self, son):
        son.father = self
        self.sons.addAsLast(son)


class BinomialHeapRelaxed:
    def __init__(self, elem, key):
        self.root = BinomialHeapNode(elem, key)

    def merge(self, otherHeap):
        thisRoot = self.root
        otherRoot = otherHeap.root

        if thisRoot.key >= otherRoot.key:
            otherRoot.fater = thisRoot
            thisRoot.addSon(otherRoot)
            return self
        else:
            thisRoot.father = otherRoot
            otherRoot.addSon(thisRoot)
            return otherHeap

    def getHeapSons(self):
        res = ListaCollegata()  # lista dei BinomialHeapRelaxed figli
        curr = self.root.sons.getFirstRecord()  # curr è un record [elem,next] dove elem è il nostro nodo
        while curr != None:
            nHeap = BinomialHeapRelaxed(None, None)
            nHeap.root = curr.elem
            nHeap.root.father = None
            res.addAsLast(nHeap)
            curr = curr.next
        return res

    def stampa(self):
        """BFS"""
        q = queue()
        # Attenzione verra' inserito 'None' come padre della radice.
        q.enqueue((None, self.root))
        while not q.isEmpty():
            father, curr = q.dequeue()
            print(father, '-->', curr.key)
            if not curr.sons.isEmpty():
                f = curr.sons.getFirstRecord()
                while f != None:
                    q.enqueue((curr.key, f.elem))
                    f = f.next


class PQbinomialHeapRelaxed:
    """Implementa una coda con priorita' tramite binomial heap.

     Questa versione ha un limite di alberi fissato.
     """
    MAXSIZE = 32  # albero di dimensione maggiore sara' B31

    def __init__(self):
        self.heap = PQbinomialHeapRelaxed.MAXSIZE * [None]
        self.max = None  # puntatore al nodo con chiave massima
        for i in range(len(self.heap)):
            self.heap[i] = []

    def insert(self, elem, key):
        """inserisce un nuovo nodo nella foresta come albero B0"""
        nHeap = BinomialHeapRelaxed(elem, key)  # nuovo B0
        root = nHeap.root
        self.heap[0].append(nHeap)
        return root

    def rebuild(self):
        """permette di fondere alberi binomiali dello stesso tipo in modo da ridurne il numero nella foresta"""
        for i in range(0, len(self.heap)):
            dim = len(self.heap[i])
            while (dim > 1):
                merged = self.heap[i][0].merge(self.heap[i][1])
                self.heap[i + 1].append(merged)
                self.heap[i].remove(self.heap[i][0])
                self.heap[i].remove(self.heap[i][0])
                dim -= 2

    def isEmpty(self):
        """verifica se l'Heap Binomiale rilassato e' vuoto oppure no"""
        for i in range(len(self.heap)):
            if self.heap[i] != []:
                return False
        return True

    def findMaxIndex(self):
        """permette di individuare l'albero la cui radice assume valore massimo nella foresta mediante due indici"""
        maxKeyListIndex = 0
        maxKeyIndex = 0
        if (self.heap[maxKeyListIndex] == []):  # nel caso in cui non esiste alcun B0 cerca la prima radice non nulla
            z = 1
            while (z < len(self.heap)):
                for r in range(0, len(self.heap[z])):
                    if (self.heap[z][r] != None):
                        maxKeyListIndex = z
                        maxKeyIndex = r
                        break
                if (maxKeyListIndex == 0 and maxKeyIndex == 0):
                    z += 1
                    continue
                elif (self.heap[maxKeyListIndex][maxKeyIndex] != None):
                    break

        for i in range(len(self.heap)):
            for j in range(len(self.heap[i])):
                if self.heap[i][j] != [] and self.heap[i][j].root.key > self.heap[maxKeyListIndex][
                    maxKeyIndex].root.key:
                    maxKeyListIndex = i
                    maxKeyIndex = j
        infoMax = [maxKeyListIndex, maxKeyIndex]
        return infoMax  # restituisce un array contenente l'indice maxKeyListIndex indicante la tipologia di albero Binomiale
        # il secondo indice maxKeyIndex restituisce la posizione della radice con chiave massima

    def findMax(self):
        """Utilizza l'array restituito da findMinIndex per aggiornare il puntatore al nodo con chiave massima"""
        index = self.findMaxIndex()
        massimo = self.heap[index[0]][index[1]].root.key
        self.max = massimo  # aggiorna il puntatore al nodo con chiave massima
        # print(f"Il massimo è {self.max} contenuto nell'albero B{index[0]}")
        return self.heap[index[0]][index[1]].root

    def stampa(self):
        """stampa tutti gli alberi binomiale costituenti l'Heap"""
        for i in range(0, len(self.heap)):
            for j in range(0, len(self.heap[i])):
                print(self.heap[i][j].root.elem, self.heap[i][j].root.key, "Radice di un albero B",i)

    def deleteMax(self):
        """elimina il nodo contenete la chiave con valore massimo dopodiche' ristruttura la foresta
         per avere meno alberi per la futura ricerca del nuovo nodo con chiave massima"""
        if self.isEmpty():
            return

        index = self.findMaxIndex()
        nuovi = self.heap[index[0]][index[1]].getHeapSons()
        self.heap[index[0]].remove(self.heap[index[0]][index[1]])
        count = 0
        curr = nuovi.getFirstRecord()

        while curr != None:
            self.heap[count].append(curr.elem)
            count += 1
            curr = curr.next
        self.rebuild()