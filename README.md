# SelfOrganizingANN

## Introduction

This is an ongoing project I'm working on to implement a neural network from scratch using custom graph and node classes. Most libraries implement neural networks using matrices even though the best way for us to think of them is as graphs of nodes and edges. For all practical purposes, the matrix implementation is far more efficient and is the way to go. However, for people new to neural networks, it would really help to see actual code that implements the structures the way they are taught using real objects instead of*__* mathematical simplifications.

## Code Overview

Implement_Graph.py defines the basic structures of the graph. Main.py contains the logic for manually carrying out backpropogation

## Future Work

I hope to complete the manual backpropogation functionality. I then plan to implement functionality to mimic some of the behaviors of the NEAT library for evolutionary algorithms. This would allow my network to modify its structure over time by generating new nodes or even entirely new layers. 