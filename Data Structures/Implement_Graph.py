import random as randIG


class Neuron:
    def __init__(self):
        self.incomingEdges = []
        self.outgoingEdges = []


class Axon:
    def __init__(self, startNode=None, endNode=None, weight=0):
        self.startNode = startNode
        self.endNode = endNode
        self.weight = weight


class Brain:
    def __init__(self):
        self.allNeurons = []
        self.allAxons = []

    def initializeBrain(self):
        inputSpawnNeuron = Neuron()
        middleSpawnNeuron = Neuron()
        outputSpawnNeuron = Neuron()
        self.formConnection(inputSpawnNeuron, middleSpawnNeuron)
        self.formConnection(middleSpawnNeuron, outputSpawnNeuron)
        self.allNeurons.extend([inputSpawnNeuron, middleSpawnNeuron, outputSpawnNeuron])

    def formConnection(self, node1, node2):
        newAxon = Axon(node1, node2)
        node1.outgoingEdges.append(newAxon)
        node2.incomingEdges.append(newAxon)
        self.allAxons.append(newAxon)






















# class Graph:
#     def __init__(self):
#         self.nodes = []
#         self.nodeCount = 0
#
#     def create_node(self, value):
#         newNode = Node(value)
#         self.add_node(newNode)
#
#     def add_node(self, newNode):
#         self.nodes.append(newNode)
#
#     def get_node(self, nodeValue):
#         return self.nodes[nodeValue-1]
#
#     def initialize_randomly(self, numNodes):
#         for i in range(numNodes):
#             self.nodeCount += 1
#             self.nodes.append(Node(self.nodeCount))
#         for startNode in self.nodes:
#             for nextNode in self.nodes:
#                 if startNode is not nextNode:
#                     coin = randIG.uniform(0, 1)
#                     if coin >= 0.5:
#                         startNode.next.append(nextNode)
#
#     def initialize_manually(self, numNodes, matrixOfNexts):
#         for i in range(numNodes):
#             self.nodeCount += 1
#             self.nodes.append(Node(self.nodeCount))
#         for index, listOfNexts in enumerate(matrixOfNexts, start=0):
#             currentNode = self.nodes[index]
#             for nextNodeIndex in listOfNexts:
#                 currentNode.next.append(self.nodes[nextNodeIndex-1])
#
#     def print_graph(self):
#         for node in self.nodes:
#             print(str(node.value) + ": " + str(node.next_values()))
#
#     def reset_graph(self):
#         for node in self.nodes:
#             node.visited = 0