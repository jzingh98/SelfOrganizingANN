from Data_Structures.Implement_Graph import Brain
from math import exp


def sigmoid(x):
    return 1 / (1 + exp(-x))


def execute_trial(startNeuron, inputValue):
    print(inputValue)
    startNeuron.inputVal = inputValue
    startNeuron.outputVal = sigmoid(startNeuron.inputVal)
    print(startNeuron.outputVal)

    print(str(startNeuron.outputVal) + " * " + str(startNeuron.outgoingEdges[0].weight))
    middleNeuron = startNeuron.outgoingEdges[0].endNode
    middleNeuron.inputVal = startNeuron.outputVal * startNeuron.outgoingEdges[0].weight
    middleNeuron.outputVal = sigmoid(middleNeuron.inputVal)
    print(middleNeuron.inputVal)
    print(middleNeuron.outputVal)

    print(str(middleNeuron.outputVal) + " * " + str(middleNeuron.outgoingEdges[0].weight))
    lastNeuron = middleNeuron.outgoingEdges[0].endNode
    lastNeuron.inputVal = middleNeuron.outputVal * middleNeuron.outgoingEdges[0].weight
    lastNeuron.outputVal = sigmoid(lastNeuron.inputVal)
    print(lastNeuron.inputVal)
    print(lastNeuron.outputVal)

    return lastNeuron.outputVal


firstBrain = Brain()
firstBrain.initializeBrain()
firstNeuron = firstBrain.startNeuron
print(execute_trial(firstNeuron, 5))
