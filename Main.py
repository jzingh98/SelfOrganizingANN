from Data_Structures.Implement_Graph import Brain
from math import exp


def sigmoid(x):
    return 1 / (1 + exp(-x))


def derivative_sigmoid(x):
    f = 1 / (1 + exp(-x))
    df = f * (1 - f)
    return df


def execute_trial(startNeuron, inputValue):
    # print(inputValue)
    startNeuron.inputVal = inputValue
    startNeuron.outputVal = sigmoid(startNeuron.inputVal)
    # print(startNeuron.outputVal)

    # print(str(startNeuron.outputVal) + " * " + str(startNeuron.outgoingEdges[0].weight))
    middleNeuron = startNeuron.outgoingEdges[0].endNode
    middleNeuron.inputVal = startNeuron.outputVal * startNeuron.outgoingEdges[0].weight
    middleNeuron.outputVal = sigmoid(middleNeuron.inputVal)
    # print(middleNeuron.inputVal)
    # print(middleNeuron.outputVal)

    # print(str(middleNeuron.outputVal) + " * " + str(middleNeuron.outgoingEdges[0].weight))
    lastNeuron = middleNeuron.outgoingEdges[0].endNode
    lastNeuron.inputVal = middleNeuron.outputVal * middleNeuron.outgoingEdges[0].weight
    lastNeuron.outputVal = sigmoid(lastNeuron.inputVal)
    # print(lastNeuron.inputVal)
    # print(lastNeuron.outputVal)

    print(lastNeuron.outputVal)
    return lastNeuron.outputVal


def execute_backpropogation(startNeuron, outputNeuron, correctY):
    error = (outputNeuron.outputVal - correctY)**2
    print(error)

    dCdW = 0
    dCdA = 0
    dAdZ = 0
    dZdW = 0

    dCdA = 2*(outputNeuron.outputVal - correctY)
    dAdZ = derivative_sigmoid(outputNeuron.inputVal)
    previousNeuron = outputNeuron.incomingEdges[0].startNode
    dZdW = previousNeuron.outputVal
    dCdW = dCdA * dAdZ * dZdW
    print(dCdW)

    adjustment = -0.1 * dCdW
    outputNeuron.incomingEdges[0].weight += adjustment

    print("\n\nFFD")
    execute_trial(startNeuron, 5)

    return



firstBrain = Brain()
firstBrain.initializeBrain()
firstNeuron = firstBrain.startNeuron
middleNeuron = firstNeuron.outgoingEdges[0].endNode
outNeuron = middleNeuron.outgoingEdges[0].endNode

print("\n\n------------------------------------\n\n")

print("\n\nFFD")
execute_trial(firstNeuron, 5)

print("\n\nBWD")
execute_backpropogation(firstNeuron, outNeuron, 1)

print("\n\n------------------------------------\n\n")

print("\n\nFFD")
execute_trial(firstNeuron, 5)

print("\n\nBWD")
execute_backpropogation(firstNeuron, outNeuron, 1)

print("\n\n------------------------------------\n\n")

print("\n\nFFD")
execute_trial(firstNeuron, 5)

print("\n\nBWD")
execute_backpropogation(firstNeuron, outNeuron, 1)

print("\n\n------------------------------------\n\n")

print("\n\nFFD")
execute_trial(firstNeuron, 5)

print("\n\nBWD")
execute_backpropogation(firstNeuron, outNeuron, 1)