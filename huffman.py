import numpy as np
import heapq

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def __lt__(self, node):
        if(not node):
            raise ValueError("Node value of NoneType cannot be compared")
        return node.value > self.value


class HuffmanTree:
    def __init__(self, fileObject):
        self.nodes = []
        self.file = fileObject

    def insert(self, value):
        newNode = Node(value)
        heapq.heappush(self.nodes, newNode)
        return newNode

    def doHuffman(self):
        while(len(self.nodes) > 1):
            node2, node1 = heapq.heappop(self.nodes), heapq.heappop(self.nodes)
            newNode = self.insert(node1.value + node2.value)
            newNode.right, newNode.left = node1, node2

    def traverse(self, node, depth = 0):
        if(not node):
            return
        self.traverse(node.left, depth = depth + 1)
        print("Depth: %s - %s" % (depth, node.value))
        self.traverse(node.right, depth = depth + 1)

    def traverseInDirection(self, node, direction):
        if(not node):
            return
        print(node.value)
        if(direction):
            self.traverse2(node.left, direction)
        else:
            self.traverse2(node.right, direction)


    def printHeap(self):
        print(self.nodes)

    def getRoot(self):
        return self.nodes[0]

    def generateHuffmanCode(self, value, node = None, hCode = ""):
        if(not node):
            return
        self.generateHuffmanCode(value, node.left, hCode = hCode + "1")
        if(node.value == value):
            self.file.write("%s\t\t%s\n" % (value, hCode))
        self.generateHuffmanCode(value, node.right, hCode = hCode + "0")

inFile = open("probabilities.txt", "r")
outFile = open("codes.txt", "w")
outFile.write("probability\tcode\n\n")
arr = []

for line in inFile:
    arr.append(float(line))

print("Number if lines in file: %s" % len(arr))

inFile.seek(0)

heapq.heapify(arr)
huffmanTree = HuffmanTree(outFile)
print(arr)

for x in range(0, len(arr)):
    huffmanTree.insert(arr[x])

huffmanTree.doHuffman()

for line in inFile:
    huffmanTree.generateHuffmanCode(float(line), huffmanTree.getRoot())

outFile.close()
