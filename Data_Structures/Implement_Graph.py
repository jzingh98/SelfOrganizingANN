import random as randGraph


class Neuron:
    def __init__(self):
        self.incomingEdges = []
        self.outgoingEdges = []
        inputVal = 0
        outputVal = 0


class Axon:
    def __init__(self, startNode=None, endNode=None):
        self.startNode = startNode
        self.endNode = endNode
        self.weight = randGraph.uniform(0, 1)


class Brain:
    def __init__(self):
        self.allNeurons = []
        self.allAxons = []
        self.startNeuron = None

    def initializeBrain(self):
        self.startNeuron = inputSpawnNeuron = Neuron()
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
